import logging
import random


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

def get_first_name(postcode: str) -> str:
    digits = [int(postcode[i:i+2]) for i in range(0, 10, 2)]
    return ''.join(chr(ord('a') + (d % 26)) for d in digits)

def get_post_code():
    number = str(random.randint(1_000_000_000, 9_999_999_999))
    return number

def find_deleted_name(first_names: list[str]) -> str:
    lengths = [len(name) for name in first_names]
    average_length = sum(lengths) / len(lengths)
    closest_name = min(first_names, key=lambda name: abs(len(name) - average_length))

    return closest_name