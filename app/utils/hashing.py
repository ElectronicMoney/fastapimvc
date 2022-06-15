from passlib.context import CryptContext


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher():

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return password_context.verify(plain_password, hashed_password)

    @staticmethod
    def create_password_hash(password):
        return password_context.hash(password)