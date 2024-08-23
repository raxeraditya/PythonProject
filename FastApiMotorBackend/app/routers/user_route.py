from fastapi import APIRouter, HTTPException
from typing import List
from app.lib.db import database
from fastapi.responses import JSONResponse
from app.models.User_Model import UserCreate


router = APIRouter()

collection = database['user']

@router.post("/register", response_model=UserCreate)
async def register_user(user: UserCreate):
    try:
        print(user)
        existing_user = await collection.find_one({"username": user.username})
        if existing_user:
            print(existing_user)
            return JSONResponse(content="user allready exists",status_code=401)
        
        user_dict = dict(user) 
        await collection.insert_one(user_dict)
        saved_user = UserCreate(
            email=user.email,
            username=user.username,
            password="*******"  
        )
        
        return saved_user
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
