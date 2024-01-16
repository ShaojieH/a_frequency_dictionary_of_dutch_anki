import csv

from paths import *

if __name__ == "__main__":

    sentence_to_audio = dict()

    with open(audio_path, encoding='UTF8') as f:
        for line in f:
            entry = line.split(maxsplit=2)
            sentence_id, audio_id = entry[0].strip(), entry[1].strip()
            sentence_to_audio[sentence_id] = audio_id

    sentence_ids = []
    with open(sentences_path, encoding='UTF8') as f:
        for line in f:
            entry = line.split(maxsplit=2)
            sentence_id = entry[0]
            sentence_ids.append(sentence_id)

    all_data = []

    for sentence_id in sentence_ids:
        audio_id = sentence_to_audio.get(sentence_id)
        if audio_id:
            all_data.append([sentence_id, audio_id])


    with open(output_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(all_data)