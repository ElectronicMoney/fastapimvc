from fastapi import APIRouter, Request
from app.controllers import AuthController
from app.schemas import AuthSchema


auth_view = APIRouter(
    prefix="/v1",
    tags=["auth"],
)

auth_controller = AuthController()

@auth_view.post("/login/")
async def login_user(auth: AuthSchema, request: Request):
    return await auth_controller.login(request, auth)

