from pymongo import MongoClient
import os


def create_mongo_client():
    mongo_uri = os.getenv('MONGO_URI')
    if not mongo_uri:
        raise ValueError("MongoDB URI not found in Config")
    client = MongoClient(mongo_uri)
    return client

