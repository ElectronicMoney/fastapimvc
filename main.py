from fastapi import  WebSocket
import uvicorn
from app import create_app
from app.settings import API_HOST, API_PORT
from app.routers import users_view, auth_view


app = create_app()

app.include_router(users_view)
app.include_router(auth_view)


@app.get("/")
async def root():
    return {"message": "Welcome Home To My Api!"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        await websocket.send_json( {"message":data})


# Run the app
if __name__ == "__main__":
    uvicorn.run("main:app", host=API_HOST, port=API_PORT, reload=True)
