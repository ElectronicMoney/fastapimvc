from app.database import Base, get_db

class Model():

    BaseModel = Base

    def __init__(self) -> None:
        self.db = get_db().__next__()

    def save(self):
        self.db.add(self)
        self.db.commit()
        self.db.refresh(self)
        return self


