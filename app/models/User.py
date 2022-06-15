from sqlalchemy import Boolean, Column, Integer, String
from .Model import Model
from app.schemas import UserSchema


model = Model()


class User(Model.BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    is_admin = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    
    def save(self):
        model.db.add(self)
        model.db.commit()
        model.db.refresh(self)
        return self

    def create_user(self, user: UserSchema):
        db_user = User(**user.dict())
        model.db.add(db_user)
        model.db.commit()
        model.db.refresh(db_user)
        return db_user

    def get_users(self):
        users = model.db.query(User).all()
        return users

    def get_user_by_id(self, id: int):
        user = model.db.query(User).get(id)
        if not user:
            return None
        return user

    def get_user_by_email(self, email: str):
        user = model.db.query(User).filter(User.email == email).first()
        return user

    def get_user_by_username(self, username: str):
        user = model.db.query(User).filter(User.username == username).first()
        return user

    def delete_user(self, id: int):
        # user = model.db.query(User).get(id)
        model.db.query(User).filter(User.id == id).delete()
        model.db.commit()
        return None





