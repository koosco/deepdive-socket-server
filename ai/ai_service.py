from config.ai_env import OPENAI_API_KEY
from openai import OpenAI


class AiService:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def translate(self, audio):
        transcription = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=audio
        )
        return transcription.text


if __name__ == "__main__":
    import asyncio


    async def main():
        client = AiService()
        audio_file = open('/Users/koo/PycharmProjects/socket-server/resources/client/test1.wav', 'br')
        result = client.translate(audio_file)
        print(result)
    asyncio.run(main())
