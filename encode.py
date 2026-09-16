import shiffConstants


def shift_letter(letter: str, shift: int) -> str:
    if not letter.isalpha():
        return letter

    code = ord(letter)

    new_code = ((code + shift) % 128)
    return chr(new_code)


def string_encode(s: str, shift: int) -> str:
    result = []
    for char in s:
        result.append(shift_letter(char, shift))
    return ''.join(result)


if __name__ == '__main__':
    print(string_encode('Hello, 123 world!', shiffConstants.positionIndex))
