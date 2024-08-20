import io
from datetime import datetime

from config.audio_env import AUDIO_STORE_URL

FILE_NAME_SUFFIX = str(datetime.now().timestamp())


def to_audio_path(file_name: str):
    return AUDIO_STORE_URL + file_name + FILE_NAME_SUFFIX + '.wav'


def to_openai_format(path: str, audio_data: bytes):
    audio_file = io.BytesIO(audio_data)
    audio_file.name = path.split('/')[-1]
    return audio_file
