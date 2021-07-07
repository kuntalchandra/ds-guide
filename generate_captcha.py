"""
Generate captcha

Generate a captcha supporting base62 of n length. The captcha must support alphanumeric values.
"""
from random import randint
from typing import List


def generate_captcha(n: int) -> str:
    if not n:
        return ""
    alphabet = (
            [chr(i) for i in range(ord("A"), ord("Z") + 1)]
            + [chr(i) for i in range(ord("a"), ord("z") + 1)]
            + [str(i) for i in range(10)]
    )
    return captcha(n, alphabet)


def captcha(n, alphabet: List[str]) -> str:
    s = ""
    for i in range(n + 1):
        s += alphabet[randint(0, 61)]
    return s


# TODO: Write the test using random seed to generate the rand instead of system time
print(generate_captcha(5))
