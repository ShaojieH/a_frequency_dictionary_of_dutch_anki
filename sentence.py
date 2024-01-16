from typing import Dict


class SentenceData:
    audio_id: str
    text: str
    # Mapping from stem to word
    stem_mappings: Dict[str, str] = {}
    translation: str = ""

    def __repr__(self) -> str:
        return f"{self.audio_id}: {self.text}, {self.stem_mappings}->{self.translation}"