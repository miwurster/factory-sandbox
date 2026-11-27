import re


def split_words(text: str) -> list[str]:
    return [word for word in re.split(r"[\s-]+", text) if word]


def reverse_words(text: str) -> str:
    return " ".join(reversed(text.split()))


def capitalize_words(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split(" "))
