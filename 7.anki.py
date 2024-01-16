import os
from pickle import load
import random
import genanki
from my_utils import check_audio

from words import WordData

from paths import word_data_path, audio_dir, sentence_audio_dir, output_deck_path

disable_autoplay = '''
<script>

var elem = document.querySelector(".soundLink, .replaybutton");

if (elem) { elem.click(); }

</script>

'''


def generate_definitions(word: WordData) -> str:

    definitions = word.definitions

    html = ""
    for definition in definitions:
        part_of_speech, inflection, meanings = definition
        html += f"<div style='margin-bottom: 10px;'>\n"
        html += f"  <span style='font-style: italic;'>{part_of_speech} </span> "
        html += f"<span style='font-weight: bold;'>{inflection}</span>\n  <ul>\n"
        for meaning in meanings:
            html += f"    <li>{meaning}</li>\n"
        html += "  </ul>\n</div>\n"
    return html


def generate_pronounciation(word: WordData)->str:
    audio_path = os.path.join(audio_dir, f"{word.word}.ogg")
    return f"[sound:{word.word}.ogg]" if check_audio(audio_path) else ""

def generate_sentences(word: WordData) -> str:
    html = ""
    for text, translation, audio in zip(word.sentences_text, word.sentences_translation, word.sentences_audio):
        html += f"<div style='text-align: center; border-bottom: 1px solid #ccc; padding-bottom: 10px; margin-bottom: 20px;'>\n"
        html += f"  <span>{text}</span> [sound:{audio}.mp3]<br/>\n"
        html += f"  <span style='color: gray;'>{translation}</span>\n"
        html += "</div>\n"
    return html

def generate_note(word: WordData)->genanki.Note:
    return genanki.Note(
        model=model,
        fields=[word.word, 
                generate_definitions(word),
                generate_pronounciation(word),
                generate_sentences(word)
        ])

model = genanki.Model(
    1614039768,
    'my model',
    fields=[
        {'name': 'dutch'},
        {'name': 'definitions'},
        {'name': 'pronounciation'},
        {'name': 'sentences'}
    ],
    templates=[{
        'name': 'card 1',
        'qfmt': '''
                <div style="text-align: center;">
                    <span style="font-size: larger;">{{dutch}}</span><br>
                    {{pronounciation}}
                </div>

                ''',
        'afmt': disable_autoplay + '{{FrontSide}}<hr id="answer">{{definitions}} {{sentences}}'
    }]
)

with open(word_data_path, 'rb') as f:

    root_deck_name = "A Frequency Dictionary of Dutch with Spoken Sentences"

    root_deck = genanki.Deck(random.randrange(1 << 30, 1 << 31), root_deck_name)
    decks = {}
    for tag in ["Core", "Fiction", "Newspapers", "Spoken", "Web", "General"]:
        decks[tag] = genanki.Deck(random.randrange(1 << 30, 1 << 31), f"{root_deck_name}::{tag}")


    all_words = load(f)
    for word in all_words:
        decks[word.subdeck].add_note(generate_note(word))

    package = genanki.Package(decks.values())
    package.media_files = [f"{audio_dir}/{word.word}.ogg" for word in all_words if check_audio(os.path.join(audio_dir, f"{word.word}.ogg"))] + [f"{sentence_audio_dir}/{audio}.mp3" for word in all_words for audio in word.sentences_audio]
    package.write_to_file(output_deck_path)