class AudioRepository:
    async def save(self, path: str, audio_file: bytes):
        with open(path, 'wb') as wav_file:
            wav_file.write(audio_file)
