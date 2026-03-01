#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2026-02-27
# Utility: Register business config to feishudb.ScrapingMongoQuery
# Environment Variables:
#   MONGO_URI - MongoDB connection URI
#   MONGO_DB - Database name (default: feishudb)
#   MONGO_COLLECTION - Collection name (default: ScrapingMongoQuery)

import json
import sys
import os
from pymongo import MongoClient

# Configuration with environment variable support
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://root:8a2p9j3x9g@13.58.80.11:30002/?tls=false')
DB_NAME = os.getenv('MONGO_DB', 'feishudb')
COLLECTION_NAME = os.getenv('MONGO_COLLECTION', 'ScrapingMongoQuery')

def register(config):
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    query = {"table": config["table"]}
    update = {"$set": config}
    result = collection.update_one(query, update, upsert=True)
    if result.upserted_id:
        print(f"✅ Successfully REGISTERED: {config['name']}")
    else:
        print(f"✅ Successfully UPDATED: {config['name']}")
    client.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 register_business.py '<json_config>'")
        sys.exit(1)
    try:
        config_data = json.loads(sys.argv[1])
        register(config_data)
    except Exception as e:
        print(f"❌ Registration failed: {e}")
