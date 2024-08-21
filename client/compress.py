from moviepy.editor import VideoFileClip

# MP4 파일 경로
input_video = "/Users/koo/PycharmProjects/socket-server/resources/client/test2.mp4"

# 추출된 오디오 파일 경로 (WAV 형식)
output_audio = "/Users/koo/PycharmProjects/socket-server/resources/client/test3.wav"

# 비디오 파일 로드
video = VideoFileClip(input_video)

# 오디오 트랙 추출
audio = video.audio

# MP3 파일로 저장 (libmp3lame 코덱 사용)
audio.write_audiofile(output_audio, codec='libmp3lame')

# 작업 완료 후 리소스 해제
audio.close()
video.close()

print(f"Audio extracted and saved as {output_audio}")