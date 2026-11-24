import re

_WORD = re.compile(r"\S+")


def reverse_words(text: str) -> str:
    words = reversed(_WORD.findall(text))
    return _WORD.sub(lambda _: next(words), text)


def capitalize_words(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split(" "))
