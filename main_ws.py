from time import sleep
from fastapi import Depends, FastAPI, WebSocket, WebSocketDisconnect

from sqlalchemy.orm import Session

from crud.process import getProcess
from db.connection import SessinLocal
from socket_connection.connection_manager import ConnectionManager

app = FastAPI()
manager = ConnectionManager()

def get_db():
    db = SessinLocal()
    try:
        yield db
    finally:
        db.close()  

@app.websocket("/ws/process")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await manager.connect(websocket)
    try:
        while True:
            sleep(5)
            with db.begin():
                process = getProcess(db)
                await websocket.send_json(process)
                json = await websocket.receive_json()
                print(json)
    except WebSocketDisconnect:
        manager.disconnect(websocket)