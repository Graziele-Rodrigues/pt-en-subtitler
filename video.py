import subprocess
import os
import whisper

# Arquivo de entrada
input_video = "video.mp4"
output_srt = "legenda.srt"
output_video = "video_subtitled.mp4"

# Incorporar legenda com ffmpeg
print("🎬 Gerando vídeo legendado...")
subprocess.run([
    "ffmpeg", "-i", input_video, "-vf", f"subtitles={output_srt}",
    "-c:a", "copy", output_video
])

print(f"✅ Vídeo com legendas salvo em: {output_video}")