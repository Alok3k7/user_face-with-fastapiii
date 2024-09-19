from fastapi import APIRouter, HTTPException, Query
from models.user import User
from config.db import client
from schemas.user import userEntity, usersEntity
from bson import ObjectId

user = APIRouter()

# Get all users
@user.get('/')
async def find_all_users():
    return usersEntity(client.db.users.find())

# Get a single user by ID, name, or email
@user.get('/search')
async def find_user(
    id: str = Query(None, alias='user_id'),
    name: str = Query(None),
    email: str = Query(None)
):
    query = {}
    if id:
        query["_id"] = ObjectId(id)
    if name:
        query["name"] = name
    if email:
        query["email"] = email
    
    if not query:
        raise HTTPException(status_code=400, detail="At least one search parameter (id, name, email) must be provided")
    
    user_data = client.db.users.find_one(query)
    if user_data:
        return userEntity(user_data)
    raise HTTPException(status_code=404, detail="User not found")

# Create a new user
@user.post('/')
async def create_user(user: User):
    new_user = dict(user)
    result = client.db.users.insert_one(new_user)
    return userEntity(client.db.users.find_one({"_id": result.inserted_id}))

# Update an existing user
@user.put('/{id}')
async def update_user(id: str, user: User):
    updated_user = dict(user)
    result = client.db.users.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": updated_user},
        return_document=True
    )
    if result:
        return userEntity(client.db.users.find_one({"_id": ObjectId(id)}))
    raise HTTPException(status_code=404, detail="User not found")

# Delete a user
@user.delete('/{id}')
async def delete_user(id: str):
    result = client.db.users.find_one_and_delete({"_id": ObjectId(id)})
    if result:
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
