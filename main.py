from AzureTTS.main import tts
from dotenv import load_dotenv
from pydub import AudioSegment

load_dotenv()

def generate_blank_audio(duration: int):
    return AudioSegment.silent(duration=duration*1000)
