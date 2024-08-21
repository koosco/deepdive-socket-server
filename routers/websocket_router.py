from fastapi import APIRouter, WebSocket, Depends, WebSocketDisconnect
from sqlalchemy.orm import Session

from service.memo_service import MemoService
from config.database import get_db

router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()
    memo_service = MemoService(db)

    data = await websocket.receive_json()
    print(data)
    audio_data = b''

    while True:
        try:
            # 청크 데이터를 수신
            chunk = await websocket.receive_bytes()
            if chunk == b'END':
                break
            audio_data += chunk
            # 청크 수신 후 응답 보내기 (필요에 따라)
            await websocket.send_text("Chunk received")
        except WebSocketDisconnect:
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            await websocket.close()
    print('loop end')
    content = await memo_service.save(data, audio_data)

    await websocket.send_text(content)
    await websocket.close()
