from fastapi import FastAPI, Request
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
from app.database import Base, engine, testing_engine
from app.errors import handle_validation_exception, handle_http_exception
from app.middlewares import AuthMiddleware


def create_app():
    # Create the database
    Base.metadata.create_all(bind=engine)
    # Model.metadata.create_all(bind=testing_engine)

    app = FastAPI()

    #Add auth middleware 
    app.add_middleware(AuthMiddleware)

    # Override the default exception handlers
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: RequestValidationError):
        return handle_http_exception(request=request, exc=exc)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
       return handle_validation_exception(request=request, exc=exc)

    # Return the app
    return app


