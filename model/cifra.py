from builtins import classmethod
from model.cifraException import CifraKeyException

class Cifra:

    @classmethod
    def encode(cls, text: str, key: int) -> str:
        if type(key) != int:
            raise CifraKeyException(key)
        if key <= 0 or key >= 26:
            raise CifraKeyException(key)
        result = ""
        for char in text.upper():
            # if ord(char) >= ord("A") and ord(char) <= ord("Z"):
            if ord("A") <= ord(char) <= ord("Z"):
                if ord(char) + key <= ord("Z"):
                    result += chr(ord(char) + key)
                else:
                    new_moviment = (ord(char) + key) - ord("Z")
                    result += chr(64 + new_moviment)
            else:
                result += "#"
        return result

    @classmethod
    def decode(cls, cifra: str, key: int) -> str:
        if type(key) != int:
            raise CifraKeyException(key)
        if key <= 0 or key >= 26:
            raise CifraKeyException(key)
        result = ""
        for char in cifra.upper():
            # A = 65 *----------*  Z = 90
            if ord("A") <= ord(char) <= ord("Z"):
                if ord(char) - key >= ord("A"):
                    result += chr(ord(char) - key)
                else:
                    new_moviment = ord("A") - (ord(char) - key)
                    result += chr(91 - new_moviment)
            else:
                result += "#"
        return result
