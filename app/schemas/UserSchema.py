from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    first_name: str  = Field(title="The first name of the user")
    last_name: str = Field(title="The last name of the user")
    username: str = Field(title="The username of the user")
    email: EmailStr = Field(title="The email of the user")
    password: str = Field(title="The password of the user")

    class Config:
        orm_mode = True

