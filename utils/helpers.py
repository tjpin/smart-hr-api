from datetime import datetime as dt
import random
import string


def random_string_id(k: int):
    return "".join(random.choices(string.ascii_lowercase, k=k))


def random_int_id(k: int):
    return int("".join(random.choices(string.digits, k=k)))


def timestamp_id(l: int):
    if l >= 20 or l <= 1:
        raise ValueError("Length must be less than 20 and grater than 1")
    id = str(dt.now().strftime("%Y%m%d%H%M%S%f"))
    id = id[::-1]  # reverse the string
    return id[slice(l)]
