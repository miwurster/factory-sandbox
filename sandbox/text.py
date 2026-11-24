def reverse_words(text: str) -> str:
    return " ".join(reversed(text.split()))


def capitalize_words(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split(" "))


def is_palindrome(text: str) -> bool:
    kept = [char.lower() for char in text if char.isalnum()]
    return kept == kept[::-1]
