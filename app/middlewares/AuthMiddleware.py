from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.database import SessionLocal
from app.errors import ApiError
from app.models.User import User
from app.models.Auth import Auth
from app.routers import routes


class AuthMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(self, request:Request, call_next):
        # do somthing before request
        if request.url.path.split("/")[2] in routes.get("auth"):
            db = SessionLocal()
            # Create user instance
            user = User()
            auth = Auth()
                # get the token from the request headers
            access_token = request.headers.get('Authorization')
            # return token
            # Check if we have token
            if access_token:
                    
                # Split the JWT Acess token to get the token
                token = access_token.split(" ")[1]
                try:
                    payload = auth.decode_jwt_token(token=token)
                    #Get The User public Id from the payload 
                    user_id = payload.get('user_id')
                    # Try to get the user using the provided token
                    auth_user = user.get_user_by_id(user_id)
                    # store the auth user object in request state
                    request.state.user = auth_user
                    # Close the db connection
                    db.close()
                except:
                    return ApiError.unauthorized("Invalid Token or Token Expired!")

            else:
                return ApiError.unauthorized("Access token is not available in the authorization heaader!")
                
        response = await call_next(request)
        # do something before response
        return response
    