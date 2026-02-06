"""
Markdown-based storage for work records.

Stores each work record as an individual Markdown file with YAML frontmatter.
Files are organized by date in a hierarchical directory structure.
"""

import os
import yaml
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional
from schema import WorkRecord, WorkType, Status


class MarkdownStorage:
    """Store and retrieve work records as Markdown files"""

    def __init__(self, base_dir: Optional[str] = None):
        """
        Initialize storage with base directory.

        Args:
            base_dir: Base directory for storing records. Defaults to ~/work-memo/
        """
        if base_dir is None:
            base_dir = os.path.expanduser("~/work-memo")

        self.base_dir = Path(base_dir)
        self.records_dir = self.base_dir / "records"
        self.records_dir.mkdir(parents=True, exist_ok=True)

    def create(self, record: WorkRecord, original_input: str = "", ai_analysis: Dict[str, Any] = None) -> str:
        """
        Create a new work record and save as Markdown file.

        Args:
            record: WorkRecord object to save
            original_input: Original user input
            ai_analysis: AI analysis results (option)

        Returns:
            str: Record ID
        """
        # Generate file path based on date and ID
        created_date = datetime.fromisoformat(record.created_at)
        year_month = created_date.strftime("%Y-%m")
        day = created_date.strftime("%d")

        # Create directory structure: YYYY-MM/DD/
        date_dir = self.records_dir / year_month / day
        date_dir.mkdir(parents=True, exist_ok=True)

        # Sanitize title for filename
        safe_title = self._sanitize_filename(record.title)
        filename = f"{record.id[:8]}_{safe_title}.md"
        filepath = date_dir / filename

        # Prepare frontmatter
        frontmatter = {
            'id': record.id,
            'title': record.title,
            'type': record.type.value,
            'status': record.status.value,
            'urgency': record.urgency,
            'importance': record.importance,
            'difficulty': record.difficulty,
            'created_at': record.created_at,
            'updated_at': record.updated_at,
        }

        # Add optional fields
        if record.description:
            frontmatter['description'] = record.description
        if record.due_date:
            frontmatter['due_date'] = record.due_date
        if record.start_date:
            frontmatter['start_date'] = record.start_date
        if record.completed_at:
            frontmatter['completed_at'] = record.completed_at
        if record.tags:
            frontmatter['tags'] = record.tags
        if record.contexts:
            frontmatter['contexts'] = record.contexts
        if record.projects:
            frontmatter['projects'] = record.projects
        if record.depends_on:
            frontmatter['depends_on'] = record.depends_on
        if record.blocks:
            frontmatter['blocks'] = record.blocks
        if record.estimated_effort:
            frontmatter['estimated_effort'] = record.estimated_effort
        if record.time_spent:
            frontmatter['time_spent'] = record.time_spent
        if record.assignee:
            frontmatter['assignee'] = record.assignee.to_dict()
        if record.reporter:
            frontmatter['reporter'] = record.reporter.to_dict()
        if record.participants:
            frontmatter['participants'] = [p.to_dict() for p in record.participants]
        if record.location:
            frontmatter['location'] = record.location.to_dict()
        if record.metadata:
            frontmatter['metadata'] = record.metadata

        # Calculate Eisenhower quadrant
        frontmatter['eisenhower_quadrant'] = record.get_eisenhower_quadrant()

        # Build content
        content_parts = []
        content_parts.append("---")
        content_parts.append(yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False))
        content_parts.append("---")
        content_parts.append("")
        content_parts.append(f"# {record.title}")
        content_parts.append("")

        # Add description if exists
        if record.description:
            content_parts.append("## Description")
            content_parts.append("")
            content_parts.append(record.description)
            content_parts.append("")

        # Add original input
        if original_input:
            content_parts.append("## Original Input")
            content_parts.append("")
            content_parts.append(f"> {original_input}")
            content_parts.append("")

        # Add AI analysis if exists
        if ai_analysis:
            content_parts.append("## AI Analysis")
            content_parts.append("")

            if 'summary' in ai_analysis:
                content_parts.append(f"**Summary:** {ai_analysis['summary']}")
                content_parts.append("")

            if 'extracted_info' in ai_analysis:
                content_parts.append("**Extracted Information:**")
                content_parts.append("")
                for key, value in ai_analysis['extracted_info'].items():
                    content_parts.append(f"- **{key}:** {value}")
                content_parts.append("")

            if 'suggestions' in ai_analysis:
                content_parts.append("**Suggestions:**")
                content_parts.append("")
                for suggestion in ai_analysis['suggestions']:
                    content_parts.append(f"- {suggestion}")
                content_parts.append("")

        # Add metadata section
        content_parts.append("## Metadata")
        content_parts.append("")
        content_parts.append(f"- **ID:** `{record.id}`")
        content_parts.append(f"- **Type:** {record.type.value}")
        content_parts.append(f"- **Status:** {record.status.value}")
        content_parts.append(f"- **Priority:** Urgency {record.urgency}/5, Importance {record.importance}/5")
        content_parts.append(f"- **Eisenhower Quadrant:** {record.get_eisenhower_quadrant()}")
        content_parts.append(f"- **Created:** {record.created_at}")
        if record.due_date:
            content_parts.append(f"- **Due Date:** {record.due_date}")
        if record.tags:
            content_parts.append(f"- **Tags:** {', '.join(['#' + t for t in record.tags])}")
        if record.contexts:
            content_parts.append(f"- **Contexts:** {', '.join(['@' + c for c in record.contexts])}")
        if record.projects:
            content_parts.append(f"- **Projects:** {', '.join(record.projects)}")

        content_parts.append("")
        content_parts.append("---")
        content_parts.append("")
        content_parts.append(f"*File: `{filepath.relative_to(self.base_dir)}`*")

        # Write to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content_parts))

        return record.id

    def get(self, record_id: str) -> Optional[WorkRecord]:
        """
        Retrieve a work record by ID.

        Args:
            record_id: Record ID

        Returns:
            WorkRecord object or None if not found
        """
        # Search for file with this ID
        for md_file in self.records_dir.rglob("*.md"):
            if md_file.stem.startswith(record_id[:8]):
                return self._load_record(md_file)
        return None

    def get_all(self) -> List[WorkRecord]:
        """
        Get all work records.

        Returns:
            List of WorkRecord objects sorted by created_at (newest first)
        """
        records = []
        for md_file in self.records_dir.rglob("*.md"):
            try:
                record = self._load_record(md_file)
                if record:
                    records.append(record)
            except Exception as e:
                print(f"Warning: Failed to load {md_file}: {e}")

        # Sort by created_at (newest first)
        records.sort(key=lambda r: r.created_at, reverse=True)
        return records

    def search(self, filters: Dict[str, Any]) -> List[WorkRecord]:
        """
        Search records based on filters.

        Args:
            filters: Dictionary of filter criteria

        Returns:
            List of matching WorkRecord objects
        """
        all_records = self.get_all()
        results = []

        for record in all_records:
            if self._matches_filters(record, filters):
                results.append(record)

        return results

    def get_by_quadrant(self, quadrant: str) -> List[WorkRecord]:
        """
        Get records by Eisenhower quadrant.

        Args:
            quadrant: Q1, Q2, Q3, or Q4

        Returns:
            List of WorkRecord objects in that quadrant
        """
        all_records = self.get_all()
        return [r for r in all_records if r.get_eisenhower_quadrant() == quadrant.upper()]

    def update(self, record: WorkRecord) -> bool:
        """
        Update an existing record.

        Args:
            record: WorkRecord object with updated data

        Returns:
            bool: True if successful
        """
        # Find existing file
        for md_file in self.records_dir.rglob("*.md"):
            if md_file.stem.startswith(record.id[:8]):
                # Update timestamp
                record.updated_at = datetime.utcnow().isoformat()

                # Re-create the file
                md_file.unlink()
                self.create(record)
                return True
        return False

    def delete(self, record_id: str) -> bool:
        """
        Delete a record.

        Args:
            record_id: Record ID

        Returns:
            bool: True if successful
        """
        for md_file in self.records_dir.rglob("*.md"):
            if md_file.stem.startswith(record_id[:8]):
                md_file.unlink()
                return True
        return False

    def close(self):
        """Close storage (no-op for file-based storage)"""
        pass

    def _load_record(self, filepath: Path) -> Optional[WorkRecord]:
        """Load a WorkRecord from a Markdown file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract frontmatter
            match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not match:
                return None

            frontmatter_str = match.group(1)
            frontmatter = yaml.safe_load(frontmatter_str)

            # Convert to WorkRecord
            record_data = {
                'id': frontmatter['id'],
                'title': frontmatter['title'],
                'type': frontmatter['type'],
                'status': frontmatter['status'],
                'urgency': frontmatter['urgency'],
                'importance': frontmatter['importance'],
                'difficulty': frontmatter.get('difficulty', 5),
                'created_at': frontmatter['created_at'],
                'updated_at': frontmatter['updated_at'],
                'description': frontmatter.get('description'),
                'due_date': frontmatter.get('due_date'),
                'start_date': frontmatter.get('start_date'),
                'completed_at': frontmatter.get('completed_at'),
                'tags': frontmatter.get('tags', []),
                'contexts': frontmatter.get('contexts', []),
                'projects': frontmatter.get('projects', []),
                'depends_on': frontmatter.get('depends_on', []),
                'blocks': frontmatter.get('blocks', []),
                'estimated_effort': frontmatter.get('estimated_effort'),
                'time_spent': frontmatter.get('time_spent'),
                'assignee': frontmatter.get('assignee'),
                'reporter': frontmatter.get('reporter'),
                'participants': frontmatter.get('participants', []),
                'location': frontmatter.get('location'),
                'metadata': frontmatter.get('metadata', {}),
            }

            return WorkRecord.from_dict(record_data)

        except Exception as e:
            print(f"Error loading record from {filepath}: {e}")
            return None

    def _matches_filters(self, record: WorkRecord, filters: Dict[str, Any]) -> bool:
        """Check if a record matches the given filters"""
        # Title/description search
        if 'title' in filters:
            search_term = filters['title'].lower()
            if search_term not in record.title.lower():
                if not record.description or search_term not in record.description.lower():
                    return False

        # Type filter
        if 'type' in filters and record.type.value != filters['type']:
            return False

        # Status filter
        if 'status' in filters and record.status.value != filters['status']:
            return False

        # Urgency filters
        if 'urgency_min' in filters and record.urgency < filters['urgency_min']:
            return False
        if 'urgency_max' in filters and record.urgency > filters['urgency_max']:
            return False

        # Importance filters
        if 'importance_min' in filters and record.importance < filters['importance_min']:
            return False
        if 'importance_max' in filters and record.importance > filters['importance_max']:
            return False

        # Tags filter (any match)
        if 'tags' in filters:
            if not any(tag in record.tags for tag in filters['tags']):
                return False

        # Contexts filter (any match)
        if 'contexts' in filters:
            if not any(ctx in record.contexts for ctx in filters['contexts']):
                return False

        # Projects filter (any match)
        if 'projects' in filters:
            if not any(proj in record.projects for proj in filters['projects']):
                return False

        # Date filters
        if 'due_date_start' in filters or 'due_date_end' in filters:
            if not record.due_date:
                return False
            due_date = datetime.fromisoformat(record.due_date)
            if 'due_date_start' in filters:
                start = datetime.fromisoformat(filters['due_date_start'])
                if due_date < start:
                    return False
            if 'due_date_end' in filters:
                end = datetime.fromisoformat(filters['due_date_end'])
                if due_date > end:
                    return False

        if 'created_at_start' in filters or 'created_at_end' in filters:
            created = datetime.fromisoformat(record.created_at)
            if 'created_at_start' in filters:
                start = datetime.fromisoformat(filters['created_at_start'])
                if created < start:
                    return False
            if 'created_at_end' in filters:
                end = datetime.fromisoformat(filters['created_at_end'])
                if created > end:
                    return False

        return True

    def _sanitize_filename(self, title: str) -> str:
        """Sanitize title for use as filename"""
        # Remove or replace invalid characters
        safe = re.sub(r'[<>:"/\\|?*]', '', title)
        # Replace spaces with underscores
        safe = safe.replace(' ', '_')
        # Limit length
        safe = safe[:50]
        # Remove trailing dots/spaces
        safe = safe.rstrip('. ')
        return safe or 'untitled'


if __name__ == "__main__":
    # Test the storage
    storage = MarkdownStorage()

    # Create a test record
    test_record = WorkRecord(
        title="Test urgent meeting",
        type=WorkType.MEETING,
        status=Status.TODO,
        urgency=5,
        importance=4,
        tags=["work", "urgent"],
        contexts=["office"],
    )

    # Save it
    record_id = storage.create(test_record, original_input="紧急会议今天 #work @office")
    print(f"Created record: {record_id}")

    # Retrieve it
    retrieved = storage.get(record_id)
    if retrieved:
        print(f"Retrieved: {retrieved.title}")
        print(f"Quadrant: {retrieved.get_eisenhower_quadrant()}")

    # Search
    results = storage.search({'urgency_min': 4})
    print(f"Found {len(results)} urgent records")
