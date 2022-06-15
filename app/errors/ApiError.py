from fastapi import status
from fastapi.responses import JSONResponse



class   ApiError():
    
    @staticmethod
    def bad_request(message: str):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error": {
                    "message": message, 
                    "type": "BAD REQUEST",
                    "code": status.HTTP_400_BAD_REQUEST
                }
            }, 
        )


    @staticmethod
    def unauthorized(message: str):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                "error": {
                    "message": message, 
                    "type": "UNAUTHORIZED",
                    "code": status.HTTP_401_UNAUTHORIZED
                }
            }, 
        )

    
    @staticmethod
    def payment_required(message: str):
        return JSONResponse(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            content={
                "error": {
                    "message": message, 
                    "type": "PAYMENT REQUIRED",
                    "code": status.HTTP_402_PAYMENT_REQUIRED
                }
            }, 
        )

    @staticmethod
    def forbidden(message: str):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={
                "error": {
                    "message": message, 
                    "type": "FORBIDDEN",
                    "code": status.HTTP_403_FORBIDDEN
                }
            }, 
        )


    @staticmethod
    def not_found(message: str):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "error": {
                    "message": message, 
                    "type": "NOT FOUND",
                    "code": status.HTTP_404_NOT_FOUND
                }
            }, 
        )

    @staticmethod
    def method_not_allowed(message: str):
        return JSONResponse(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            content={
                "error": {
                    "message": message, 
                    "type": "METHOD NOT ALLOWED",
                    "code": status.HTTP_405_METHOD_NOT_ALLOWED
                }
            }, 
        )

    @staticmethod
    def conflict(message: str):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "error": {
                    "message": message, 
                    "type": "CONFLICT",
                    "code": status.HTTP_409_CONFLICT
                }
            }, 
        )

    @staticmethod
    def internal_server(message: str):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error": {
                    "message": message, 
                    "type": "INTERNAL SERVER ERROR",
                    "code": status.HTTP_500_INTERNAL_SERVER_ERROR
                }
            }, 
        )