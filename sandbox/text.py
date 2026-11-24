import re


def reverse_words(text: str) -> str:
    words = reversed(re.findall(r"\S+", text))
    return re.sub(r"\S+", lambda _: next(words), text)


def capitalize_words(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split(" "))
