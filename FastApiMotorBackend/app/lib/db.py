from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

# Database connection settings
MONGO_URL = "mongodb://localhost:27017"
DATABASE_NAME = "mydatabase"

client = AsyncIOMotorClient(MONGO_URL)
database = client[DATABASE_NAME]
