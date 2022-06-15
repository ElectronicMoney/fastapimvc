from pydantic import BaseModel, Field


class AuthSchema(BaseModel):
    username: str = Field(title="The username of the user")
    password: str = Field(title="The password of the user")

    class Config:
        orm_mode = False
