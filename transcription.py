from pydub.utils import which
from pydub import AudioSegment
import speech_recognition as sr

# Defina o caminho do ffmpeg
AudioSegment.converter = which("ffmpeg")
AudioSegment.ffmpeg = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")


def transcribe_audio(file_path):
    # Inicializa o reconhecedor de fala
    recognizer = sr.Recognizer()

    try:
        # Carrega o arquivo de áudio usando Pydub
        audio = AudioSegment.from_file(file_path)

        # Salva o arquivo temporariamente em um formato compatível com SpeechRecognition
        temp_file_path = "temp_audio.wav"
        audio.export(temp_file_path, format="wav")

        # Lê o arquivo de áudio usando SpeechRecognition
        with sr.AudioFile(temp_file_path) as source:
            audio_data = recognizer.record(source)
            transcription = recognizer.recognize_google(audio_data, language="pt-BR")  # Você pode mudar o idioma aqui

        return transcription

    except FileNotFoundError as e:
        print(f"Erro de arquivo não encontrado: {e}")
        return None
    except sr.UnknownValueError:
        print("O reconhecimento de fala não conseguiu entender o áudio.")
        return None
    except sr.RequestError as e:
        print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala: {e}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao tentar transcrever o áudio: {e}")
        return None
