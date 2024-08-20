from fastapi import APIRouter, WebSocket, Depends
from sqlalchemy.orm import Session

from service.memo_service import MemoService
from config.database import get_db

router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()
    memo_service = MemoService(db)
    data = await websocket.receive_json()
    audio_data = await websocket.receive_bytes()
    await memo_service.save(data, audio_data)
    await websocket.send_text('audio data received successfully')
