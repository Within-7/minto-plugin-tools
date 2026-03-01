#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2026-02-27
# Utility: Delete project from projectdb.projectdb (Pyspider Core DB)
# Environment Variables:
#   MONGO_URI - MongoDB connection URI
#   MONGO_DB - Database name (default: projectdb)
#   MONGO_COLLECTION - Collection name (default: projectdb)

import sys
import os
from pymongo import MongoClient

# Configuration with environment variable support
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://root:8a2p9j3x9g@13.58.80.11:30002/?tls=false')
DB_NAME = os.getenv('MONGO_DB', 'projectdb')
COLLECTION_NAME = os.getenv('MONGO_COLLECTION', 'projectdb')

def delete_project(project_name):
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    
    # 执行删除
    result = collection.delete_one({"name": project_name})
    
    if result.deleted_count > 0:
        print(f"🗑️  Successfully DELETED project from Database: {project_name}")
    else:
        print(f"⚠️  Project not found in Database: {project_name}")
    
    client.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 delete_project.py <project_name>")
        sys.exit(1)
        
    project_name = sys.argv[1]
    delete_project(project_name)
