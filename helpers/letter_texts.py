import random
import string


def generate_text(
        length: int
) -> str:
    text = string.ascii_letters + string.digits + ' .' * 2
    random_text_string = ''.join(
        random.choices(
            text,
            k=length
        )
    )
    return random_text_string
