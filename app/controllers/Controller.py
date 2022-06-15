from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response


class Controller():

    def response(self, data, code):
        if data == None:
            return Response(status_code=code)

        return JSONResponse(content=jsonable_encoder(data), status_code=code)
