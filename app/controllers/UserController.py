from fastapi import Request, status
from app.errors import ApiError
from app.models import User
from app.utils.hashing import Hasher
from app.schemas import UserSchema
from .Controller import Controller


class UserController(Controller):

    def __init__(self):
        self.user = User()


    async def get(self, request: Request):
        data =  self.user.get_users()
        return self.response(data=data, code=status.HTTP_200_OK)

    async def show(self, request: Request, id: int):
        user = self.user.get_user_by_id(id)
        if not user:
            return ApiError.not_found("User not found for the given Id: {}".format(id))
        # Return the user response
        return self.response(data=user, code=status.HTTP_200_OK)


    async def post(self, request: Request,  user: UserSchema):

        # Check if the username alredy exist
        db_user_by_username = self.user.get_user_by_username(user.username)

        if db_user_by_username:
            return ApiError.bad_request("Username already registered!")

        # Check if the email alredy exist
        db_user_by_email = self.user.get_user_by_email(user.email)

        if db_user_by_email:
            return ApiError.conflict("Email already registered")

        self.user.first_name = user.first_name
        self.user.last_name = user.last_name
        self.user.username = user.username
        self.user.email = user.email
        self.user.password = Hasher.create_password_hash(user.password)

        new_user = self.user.save()
        # Return ressponse
        return self.response(data=new_user, code=status.HTTP_201_CREATED)

    async def update(self, request: Request, id: int):
        # Get the ussserr using the id
        user = self.user.get_user_by_id(id)
        request_user = await request.json()

        if "first_name" in request_user:
            user.first_name =  request_user.get("first_name")
        
        if "last_name" in request_user:
            user.last_name =  request_user.get("last_name")

        user.save()
        return self.response(data=user, code=status.HTTP_200_OK)


    async def delete(self, request: Request, id: int):
        self.user.delete_user(id)
        return self.response(data=None, code=status.HTTP_204_NO_CONTENT)


