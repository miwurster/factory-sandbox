def reverse_words(text: str) -> str:
    return " ".join(reversed(text.split()))


def capitalize_words(text: str) -> str:
    return " ".join(word[:1].upper() + word[1:] for word in text.split(" "))
