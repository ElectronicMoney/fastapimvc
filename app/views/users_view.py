from fastapi import APIRouter, Request
from app.controllers import UserController
from app.schemas import UserSchema



users_view = APIRouter(
    prefix="/v1",
    tags=["users"],
)


user_controller = UserController()

@users_view.post("/register/")
async def create_user(user: UserSchema, request: Request):
    return await user_controller.post(request, user)

@users_view.get("/users/")
async def get_all_users(request: Request):
    return await user_controller.get(request)

@users_view.get("/users/{id}")
async def get_user_by_id(request: Request, id: int):
    return await  user_controller.show(request, id)

@users_view.patch("/users/{id}")
async def update_users(request: Request, id: int):
    return await  user_controller.update(request, id)

@users_view.delete("/users/{id}")
async def delete_users(request: Request, id: int):
    return await  user_controller.delete(request, id)

