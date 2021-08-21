import string
from random import choice


def get_random_email(length: int) -> str:
    address = get_random_string(length)
    provider = get_random_string(length)
    return f"{address}@{provider}.com"


def get_random_string(length: int) -> str:
    letters = string.ascii_lowercase
    result_str = "".join(choice(letters) for i in range(length))
    return result_str