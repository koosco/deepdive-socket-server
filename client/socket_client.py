import asyncio
import websockets
import base64


async def send_audio_file(uri: str, title: str, audio_file_path: str):
    async with websockets.connect(uri) as websocket:
        file_name = audio_file_path.split('/')[-1].split('.')[0]
        await websocket.send(f'{{"file_name": "{file_name}", "title": "{title}"}}')
        with open(audio_file_path, "rb") as audio_file:
            audio_data = audio_file.read()
            await websocket.send(audio_data)
            print(f"Sent audio data.")

        response = await websocket.recv()
        print(f"Received response from server: {response}")


if __name__ == '__main__':
    # WebSocket 서버 URI와 테스트용 파일 경로
    uri = "ws://localhost:8000/ws"
    title = "Test Audio"
    audio_file_path = '/Users/koo/PycharmProjects/socket-server/resources/client/test1.wav'

    # 비동기 함수 실행
    asyncio.get_event_loop().run_until_complete(send_audio_file(uri, title, audio_file_path))
