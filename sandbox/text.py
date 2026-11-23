import re


def reverse_words(text: str) -> str:
    return " ".join(reversed(text.split()))


def capitalize_words(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split(" "))


def slugify(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", text).lower().strip("-")
