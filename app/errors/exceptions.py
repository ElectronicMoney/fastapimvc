from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError



async def handle_http_exception(request: Request, exc:RequestValidationError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {"message": str(exc.detail), "status_code": exc.status_code}
        }, 
    )



async def handle_validation_exception(request: Request, exc: RequestValidationError):
        errors = []
        for err in exc.errors():
            error = { "message" : "{} {}".format(err.get("loc")[1], err.get("msg"))}
            errors.append(error)
            
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder({
                "error": {
                    "errors": errors, 
                    "status_code": status.HTTP_400_BAD_REQUEST
                } 
            }),
        )

