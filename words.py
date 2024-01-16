from typing import List


class WordData:
    word: str
    stem: str

    subdeck: str = "" # For anki

    definitions: List = []

    sentences_text: List[str] = []
    sentences_translation: List[str] = []
    sentences_audio: List[str] = []

    def __init__(self, word) -> None:
        self.word = word

    def __repr__(self) -> str:
        return f"{self.subdeck}, {self.word}, {self.stem}, {self.definitions}"