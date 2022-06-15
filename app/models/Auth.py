from app.models.User import User
import jwt
import datetime
from app.settings import SECRETE_KEY



class Auth():

    def __init__(self) -> None:
        self.user = User()
        self.secrete_key = SECRETE_KEY

    def encode_jwt_token(self, user_id: int) -> dict:
                # Set the payload; which is the profile
        exp_date = datetime.datetime.utcnow() + datetime.timedelta(days=365)

        payload = {
            'user_id': user_id,
            'exp': exp_date
        } 
        # Emcode the payload using the secrete key
        token = jwt.encode(payload, self.secrete_key, algorithm="HS256")
        # return the dictionary containing the token
        return {"token": token}


    def decode_jwt_token(self, token: str) -> dict:
        try:
            decoded_token = jwt.decode(token, self.secrete_key, algorithms=["HS256"])
            return decoded_token
        except:
            # Signature has expired
            return None

