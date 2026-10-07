import shiffConstants


def string_decode(message: str, shift: int = shiffConstants.positionIndex) -> str:
    out = ""
    for i in message:
        if 'a' <= i <= 'z':
            base = ord('a')
        elif 'A' <= i <= 'Z':
            base = ord('A')
        else:
            out += i
            continue

        decimal = (ord(i) - base - shift) % 26 + base
        out += chr(decimal)     
    return out