from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pymongo import MongoClient
from bson import ObjectId
import os

app = FastAPI()

# Connect to MongoDB
MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client.myapp

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

@app.get("/api/users")
def get_users():
    users = list(db.users.find({}, {"_id": 0}))
    return {"users": users}

@app.post("/api/users")
def create_user(user: dict):
    db.users.insert_one(user)
    return {"message": "User created", "user": user}

@app.get("/api/users/{email}")
def get_user(email: str):
    user = db.users.find_one({"email": email}, {"_id": 0})
    return user if user else {"error": "User not found"}