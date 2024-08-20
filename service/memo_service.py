from sqlalchemy.orm import Session

from ai.ai_service import AiService
from repository.audio_repository import AudioRepository
from repository.memo_repository import MemoRepository
from utils.converter import to_audio_path, to_openai_format


class MemoService:
    def __init__(self, db: Session):
        self.ai_service = AiService()
        self.memo_repository = MemoRepository(db)
        self.audio_repository = AudioRepository()

    async def save(self, data: dict | None, audio_data: bytes):
        path = to_audio_path(data['file_name'])
        audio_file = to_openai_format(path, audio_data)
        content = self.ai_service.translate(audio_file)
        await self.audio_repository.save(path, audio_data)

        self.memo_repository.save(data['title'], content)
