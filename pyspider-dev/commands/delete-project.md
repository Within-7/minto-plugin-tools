---
description: Delete crawler from MongoDB projectdb and clean up files
args:
  - name: project_name
    description: Crawler project name to delete
    required: true
---

# Delete Project

Delete crawler from MongoDB projectdb and clean up files with proper synchronization.

## Process

1. **Confirm Deletion**: Verify project name and dependencies

2. **Physical Delete**: Remove Python script file

3. **Git Sync**: Commit deletion to repository

4. **Database Cleanup**: Remove from projectdb collection

## Examples

```bash
# Delete a project
/delete-project TikTokByKeywords

# Delete multiple projects (run multiple times)
/delete-project FacebookAds
/delete-project YoutubeVideo
```

## Deletion Steps

### Step 1: Physical Delete
Remove the Python script file:
```bash
rm [ProjectName].py
```

### Step 2: Git Sync
Commit the deletion to repository:
```bash
git add .
git commit -m "feat: remove [ProjectName] crawler"
git push
```

### Step 3: Database Cleanup
Remove from MongoDB projectdb:
```bash
python3 skills/production-sop/scripts/delete_project.py [ProjectName]
```

## Environment Variables

Optional environment variables for database connection:

```bash
export MONGO_URI='mongodb://user:pass@host:port/?tls=false'
export MONGO_DB='projectdb'
export MONGO_COLLECTION='projectdb'
```

**Defaults**:
- `MONGO_URI`: Production database URI
- `MONGO_DB`: projectdb
- `MONGO_COLLECTION`: projectdb

## Verification

After deletion, verify:

1. **File Deleted**:
   ```bash
   ls [ProjectName].py
   # Should return: No such file or directory
   ```

2. **Git Committed**:
   ```bash
   git log --oneline -1
   # Should show deletion commit
   ```

3. **Database Cleaned**:
   ```bash
   mongo projectdb --eval 'db.projectdb.findOne({name: "ProjectName"})'
   # Should return: null
   ```

## Pre-Deletion Checklist

Before deleting, verify:

- [ ] Project is no longer needed
- [ ] No active tasks are running
- [ ] Data has been archived if needed
- [ ] No other projects depend on this crawler
- [ ] Team members are notified

## Common Issues

**Issue**: Script not found
- **Solution**: Verify project name matches filename exactly
- **Solution**: Check current directory

**Issue**: Database deletion fails
- **Solution**: Check `MONGO_URI` environment variable
- **Solution**: Verify database permissions

**Issue**: Git push fails
- **Solution**: Check git remote configuration
- **Solution**: Resolve any merge conflicts

## Related Operations

**Register a new crawler**:
```bash
/register-db '{"name":"NewCrawler","table":"new_key","mapping":{...}}'
```

**Create a new crawler**:
```bash
/new-crawler NewCrawler ./new_crawler.py
```

**Create strategy crawler**:
```bash
/strategy-crawler NewCrawler A ./new_crawler.py
```

## See Also

- `/register-db` - Register new crawler to database
- `production-sop` skill - Database operations guide
- `DATABASE_OPS_GUIDE.md` - Complete database documentation
