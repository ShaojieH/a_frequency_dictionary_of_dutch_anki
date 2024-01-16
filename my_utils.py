# Renamed from utils.py for collision with wiktionaryparser
import os


def check_audio(audio_path) -> bool:
    if not os.path.exists(audio_path):
        return False
    
    file_size = os.path.getsize(audio_path)
    return file_size > 0