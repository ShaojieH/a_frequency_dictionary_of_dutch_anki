from typing import List, Set
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize

stemmer = SnowballStemmer("dutch")

def get_tokens(sentence: str)->List[str]:
    tokens = word_tokenize(sentence, language='dutch')
    return tokens

def get_stem(token: str)->str:
    return stemmer.stem(token)

def get_stems(sentence: str)->Set[str]:
    tokens = get_tokens(sentence)
    tokens=[token for token in tokens if token.isalpha()]
    return set([stemmer.stem(token) for token in tokens])
