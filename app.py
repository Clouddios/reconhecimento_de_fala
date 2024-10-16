from flask import Flask, request, render_template, send_from_directory
from transcription import transcribe_audio
from export_utils import save_to_docx, save_to_pdf
import os

app = Flask(__name__)

# Verifica se o diretório "audio" existe e cria, se não existir
if not os.path.exists('audio'):
    os.makedirs('audio')

# Verifica se o diretório "exports" existe e cria, se não existir
if not os.path.exists('exports'):
    os.makedirs('exports')

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        audio_file = request.files['file']
        file_path = os.path.join("audio", audio_file.filename)
        audio_file.save(file_path)

        transcription = transcribe_audio(file_path)

        save_to_docx(transcription, "transcricao")
        save_to_pdf(transcription, "transcricao")

        return f"Transcrição realizada com sucesso! <br>Texto: {transcription}"

    return render_template('upload.html')

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory('exports', filename)

if __name__ == "__main__":
    app.run(debug=True)
