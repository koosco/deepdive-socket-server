import io
from datetime import datetime

from config.audio_env import AUDIO_STORE_URL

FILE_NAME_SUFFIX = ''.join(str(datetime.now().timestamp()).replace('.', '_'))


def to_audio_path(file_name: str):
    file_name, file_type = file_name.split('.')
    return AUDIO_STORE_URL + file_name + "_" + FILE_NAME_SUFFIX + "." + file_type


def to_openai_format(path: str, audio_data: bytes):
    audio_file = io.BytesIO(audio_data)
    audio_file.name = path.split('/')[-1]
    return audio_file
