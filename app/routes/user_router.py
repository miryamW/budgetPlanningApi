from fastapi import FastAPI, Depends, APIRouter, HTTPException
from app.services import users_service
from app.models.user import User

user_router = APIRouter()


@user_router.post("/signIn")
async def signin(user: User):
    is_sign_in = await users_service.signin(user)
    if is_sign_in:
        return "you were signed in successfully"
    raise HTTPException(status_code=404, detail="this user is not exist")


@user_router.post("/signUp")
async def signup(user: User):
    is_sign_up = await users_service.signup(user)
    if is_sign_up:
        return "you were signed up successfully"
    raise HTTPException(status_code=400, detail="one or more of your details was not valid, please try again")


@user_router.put("/setProfile/{id}")
async def update_profile(user_id: int, user: User):
    is_updated = await users_service.update_user_profile(user_id, user)
    if is_updated:
        return "your profile were updated successfully"
    raise HTTPException(status_code=400, detail="one or more of your details was not valid, please try again")