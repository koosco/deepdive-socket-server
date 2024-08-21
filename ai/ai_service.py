import io

from config.ai_env import OPENAI_API_KEY
from openai import OpenAI


class AiService:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def translate(self, audio):
        print('audio=', audio)
        transcription = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=audio
        )
        return transcription.text

    def summary(self, text: str):
        pass
