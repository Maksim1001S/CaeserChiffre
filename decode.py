import shiffConstants

def decode(message : str) -> str:
    out = ""
    for i in message:
        decimal = ord(i)
        decimal = decimal - shiffConstants.positionIndex
        out = out + chr(decimal)
    return out