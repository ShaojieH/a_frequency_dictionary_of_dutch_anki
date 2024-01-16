import os
import pickle
from nlp import get_stem
from playsound import playsound

with open("data/word_data.pkl", "rb") as f:
    all_words = pickle.load(f)

if __name__ == "__main__":

    print("Ready.")

    while True:
        stem = get_stem(input())
        matched = next((word for word in all_words if word.stem == stem), None)

        if matched:
            for text, translation, audio in zip(
                matched.sentences_text,
                matched.sentences_translation,
                matched.sentences_audio,
                ):
                print(f"{text}->{translation}")

                audio_path = os.path.join("data", "audio", f"{audio}.mp3")
                playsound(audio_path)