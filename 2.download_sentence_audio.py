import os
import requests

from paths import output_path

from tqdm.contrib.concurrent import process_map

from utils import check_audio

audio_url = "https://tatoeba.org/audio/download/{audio_id}"
audio_dir = "data/audio"

NUM_PROCESSES = 4


def download_audio(line: str) -> str:

    audio_id = line.split(',')[1].strip()
    audio_path = os.path.join(audio_dir, f"{audio_id}.mp3")

    if check_audio(audio_path):
        return audio_path

    url = audio_url.format(audio_id=audio_id)
    resp = requests.get(url)

    with open(audio_path, "wb") as f: 
        f.write(resp.content)

    print(audio_path)

    return audio_path

if __name__ == "__main__":

    with open(output_path) as f:
        lines = f.readlines()
        r = process_map(download_audio, lines, max_workers=NUM_PROCESSES, total=len(lines), chunksize=1)
