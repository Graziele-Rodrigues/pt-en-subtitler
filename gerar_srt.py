import whisper
import subprocess
import os

def write_srt(result, filename="legenda.srt"):
    with open(filename, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result["segments"], start=1):
            start = segment["start"]
            end = segment["end"]

            # Função para formatar timestamp no padrão SRT
            def format_timestamp(seconds: float):
                hours = int(seconds // 3600)
                minutes = int((seconds % 3600) // 60)
                secs = int(seconds % 60)
                millis = int((seconds * 1000) % 1000)
                return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

            f.write(f"{i}\n")
            f.write(f"{format_timestamp(start)} --> {format_timestamp(end)}\n")
            f.write(f"{segment['text'].strip()}\n\n")

# Arquivo de entrada
input_video = "video.mp4"
output_srt = "legenda.srt"

# Carregar modelo Whisper
print("🔄 Transcrevendo e traduzindo...")
model = whisper.load_model("small")
result = model.transcribe(input_video, task="translate")

# Gerar SRT em inglês
print("💾 Salvando legenda...")
write_srt(result, output_srt)

