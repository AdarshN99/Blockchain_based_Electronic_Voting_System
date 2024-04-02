from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["elections"]

# Create 'admins' collection
admin = db["admin"]
admin.create_index([("username", 1)], unique=True)


# Create 'electionlists' collection
electionlists = db["electionlists"]
electionlists.create_index([("election_id", 1)], unique=True)

# Insert sample data into 'admins' collection
admin_data = [
    {"username": "admin1", "password": "password1"},
    {"username": "admin2", "password": "password2"},
]
result = admin.insert_many(admin_data)
print(f"Inserted {len(result.inserted_ids)} admin.")

# Insert sample data into 'electionlists' collection
electionlist_data = [
    {"election_id": 1, "election_name": "Presidential Election", "election_organizer": "Government", "election_password": "password123"},
    {"election_id": 2, "election_name": "Mayoral Election", "election_organizer": "City Council", "election_password": "password456"},
]
result = electionlists.insert_many(electionlist_data)
print(f"Inserted {len(result.inserted_ids)} election lists.")