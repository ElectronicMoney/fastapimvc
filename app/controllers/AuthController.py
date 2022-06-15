from fastapi import Request, status
from .Controller import Controller
from app.errors import ApiError
from app.models import User
from app.models import Auth
from app.utils.hashing import Hasher
from app.schemas import AuthSchema
from app.utils.hashing import Hasher


class AuthController(Controller):
    def __init__(self) -> None:
        self.user = User()
        self.auth = Auth()



    async def login(self, request: Request,  auth: AuthSchema):
        # Try to get the user using the provided username
        user = self.user.get_user_by_username(auth.username)
        # Check if not the User
        if not user:
            return ApiError.unauthorized("The Username or password is Incorrect!")

        # Check if the user is active
        if not user.is_active:
            return ApiError.forbidden("Your Account have been suspended; please contact support!")

        # verify the password
        if not Hasher.verify_password(auth.password, user.password):
            return ApiError.forbidden("The Username or password is Incorrect!")

        auth_token = self.auth.encode_jwt_token(user_id=user.id)
        return self.response(data=auth_token, code=status.HTTP_200_OK)

