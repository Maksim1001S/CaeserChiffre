import shiffConstants
import decode


def shift_letter(letter: str, shift: int) -> str:
    if 'a' <= letter <= 'z':
        base = ord('a')
    elif 'A' <= letter <= 'Z':
        base = ord('A')
    else:
        return letter

    return chr((ord(letter) - base + shift) % 26 + base)


def string_encode(s: str, shift: int) -> str:
    result = []
    for char in s:
        result.append(shift_letter(char, shift))
    return ''.join(result)


if __name__ == '__main__':
    print(string_encode('Hello, 123 world!', shiffConstants.positionIndex))
    print(decode.string_decode(string_encode('Hello, 123 world!', shiffConstants.positionIndex)))
    
