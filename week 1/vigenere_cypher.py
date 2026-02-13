import sys
from typing import Tuple, List


def read_input() -> Tuple[List[str], List[str]]:
    """
    Reads cipher instructions and plaintext sentences from the command line.

    Returns:
        Tuple[List[str], List[str]]:
            - A list of cipher specifiers
            - A list of input sentences to process.
    """
    cipher = input().split()
    specifier, key = cipher

    plaintext: List[str] = []

    for sentence in sys.stdin:
        plaintext.append(sentence)

    return specifier, key, plaintext


def apply_vigenere_key(is_encrypt: bool, key: str, key_index: int, sentence: str):
    result = ""
    text_index = 0

    if is_encrypt:
        sign = 1
    else:
        sign = -1

    while text_index < len(sentence):
        cur_letter = sentence[text_index]

        if cur_letter.isalpha():
            if cur_letter.isupper():
                cur_letter = cur_letter.lower()
                is_upper_case = True
            else:
                is_upper_case = False

            cur_key = key[key_index]

            shift = (ord(cur_key) - ord('a')) * sign

            target = chr((ord(cur_letter) - ord('a') + shift) % 26 + ord('a'))

            if is_upper_case:
                target = target.upper()

            result += target

            key_index = (key_index + 1) % len(key)
        else:
            result += cur_letter

        text_index += 1

    return result, key_index


def main() -> None:
    """
    Main program execution:
        - Reads input
        - Generates composed cipher mapping
        - Applies substitution to each sentence
    """
    specifier, key, plaintext = read_input()

    if specifier == "e":
        is_encrypt: bool = True
    else:
        is_encrypt: bool = False

    key_index = 0

    for sentence in plaintext:
        result, key_index = apply_vigenere_key(is_encrypt, key, key_index, sentence)
        sys.stdout.write(result)


if __name__ == "__main__":
    main()
