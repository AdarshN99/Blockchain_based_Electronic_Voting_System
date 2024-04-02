from pymongo import MongoClient

# Connect to your MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["voting_system"]

# Create indexes on the 'name' field for both users and admins collections
db.users.create_index([("name", 1)], unique=True)
db.admins.create_index([("name", 1)], unique=True)