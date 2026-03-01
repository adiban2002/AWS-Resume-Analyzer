import re
def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9+.#/ ]", "", text)
    return text.strip()


def tokenize(text: str):
    return text.split()


def unique_tokens(tokens):
    return list(set(tokens))