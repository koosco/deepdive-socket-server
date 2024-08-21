import asyncio
import websockets


async def send_audio_file(uri: str, title: str, audio_file_path: str, chunk_size: int = 1024):
    async with websockets.connect(uri) as websocket:
        file_name = audio_file_path.split('/')[-1]
        await websocket.send(f'{{"file_name": "{file_name}", "title": "{title}"}}')
        print(f"Sent metadata: file_name={file_name}, title={title}")

        with open(audio_file_path, "rb") as audio_file:
            idx = 1
            while True:
                chunk = audio_file.read(chunk_size)
                if not chunk:
                    break
                await websocket.send(chunk)
                print(f"Sent a chunk of size: {len(chunk)} bytes")

                # 서버 응답 대기 (선택 사항)
                response = await websocket.recv()
                print(f"Received {idx} response from server: {response}")
                idx += 1
        await websocket.send(b'END')
        print("Finished sending audio file.")
        response = await websocket.recv()
        print('최종 결과는')
        print(f"Received response from server: {response}")


if __name__ == '__main__':
    uri = "ws://localhost:8000/ws"
    title = "Test Audio"
    audio_file_path = '/Users/koo/PycharmProjects/socket-server/resources/client/test2.mp3'
    chunk_size = 1024 * 1024  # 1KB씩 전송

    # 비동기 함수 실행
    asyncio.get_event_loop().run_until_complete(send_audio_file(uri, title, audio_file_path, chunk_size))
