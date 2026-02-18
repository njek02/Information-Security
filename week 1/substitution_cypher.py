import sys
from typing import Tuple, List, Dict


def read_input() -> Tuple[List[str], List[str]]:
    """
    Reads cipher instructions and plaintext sentences from the command line.

    Returns:
        Tuple[List[str], List[str]].
    """
    cipher_str: List[str] = input().split()
    sentences: List[str] = []

    for sentence in sys.stdin:
        sentences.append(sentence)

    return cipher_str, sentences


def generate_cipher(cipher_str: List[str]) -> Dict[str, str]:
    """
    Generates a substitution mapping dictionary based on a sequence
    of encryption/decryption operations.

    Args:
        cipher_str (List[str])

    Returns:
        Dict[str, str]
    """
    letter_map: Dict[str, str] = {
        char: char for char in "abcdefghijklmnopqrstuvwxyz"
    }

    i = 0
    while i < len(cipher_str):
        specifier: str = cipher_str[i]  # a decryption or encryption specifier
        cipher: str = cipher_str[i + 1]  # a shift or mapping cipher

        if cipher.isdigit():
            shift: int = int(cipher)
            if specifier == "d":
                shift = -shift
            apply_shift(letter_map, shift)
        else:
            decrypt: bool = specifier == "d"
            apply_mapping(letter_map, cipher, decrypt)

        i += 2

    return letter_map


def apply_shift(letter_map: Dict[str, str], shift: int) -> None:
    """
    Applies a shift to the values of the current mapping.

    Args:
        letter_map (Dict[str, str])
        shift (int)
    """
    for key in letter_map:
        letter_map[key] = chr(
            (ord(letter_map[key]) - ord("a") + shift) % 26 + ord("a")
        )


def apply_mapping(
    letter_map: Dict[str, str],
    mapping: str,
    decrypt: bool
) -> None:
    """
    Applies a substitution mapping to the current mapping values.
    Supports both encryption and decryption.

    Args:
        letter_map (Dict[str, str])
        mapping (str)
        decrypt (bool)
    """
    temp_map: Dict[str, str] = dict(zip("abcdefghijklmnopqrstuvwxyz", mapping))

    if decrypt:
        temp_map = {v: k for k, v in temp_map.items()}

    for key in letter_map:
        letter_map[key] = temp_map[letter_map[key]]


def apply_substitution(
    sentence: str,
    letter_map: Dict[str, str]
) -> None:
    """
    Applies the final substitution mapping to a sentence and writes
    the transformed text to stdout.

    Args:
        sentence (str)
        letter_map (Dict[str, str])
    """
    target_string: str = ""

    for char in sentence:
        if char.isalpha():
            if char.isupper():
                target_char = letter_map[char.lower()].upper()
            else:
                target_char = letter_map[char]
        else:
            target_char = char

        target_string += target_char

    sys.stdout.write(target_string)


def main() -> None:
    """
    Reads input.
    Generates composed cipher mapping.
    Applies substitution to each sentence.
    """
    cipher_str, plaintext = read_input()
    letter_map = generate_cipher(cipher_str)

    for sentence in plaintext:
        apply_substitution(sentence, letter_map)


if __name__ == "__main__":
    main()
