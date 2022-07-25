from abc import ABC, abstractmethod
import string


class Rot(ABC):
    @abstractmethod
    def encode(self, text: str) -> str:
        pass

    @abstractmethod
    def decode(self, text: str) -> str:
        pass

    @abstractmethod
    def rot_type(self) -> str:
        pass


class Rot13(Rot):
    def __init__(self):
        self._shift = 13
        self._type: str = "rot" + str(self._shift)

    def encode(self, text: str) -> str:
        return Cipher.encrypt(text, self._shift)

    def decode(self, text: str) -> str:
        return Cipher.decrypt(text, self._shift)

    def rot_type(self) -> str:
        return self._type


class Rot47(Rot):
    def __init__(self):
        self._shift = 47
        self._type: str = "rot" + str(self._shift)

    def encode(self, text: str) -> str:
        return Cipher.encrypt(text, self._shift)

    def decode(self, text: str) -> str:
        return Cipher.decrypt(text, self._shift)

    def rot_type(self) -> str:
        return self._type


class Cipher:
    @staticmethod
    def encrypt(text: str, count: int) -> str:
        result = ""
        for word in text:
            for char in word:
                temp = ord(char) + count
                if ord(char) == 32:
                    result += " "
                if temp > 126:
                    temp -= 94
                    result += chr(temp)
                else:
                    result += chr(temp)

        return result

    @staticmethod
    def decrypt(text: str, count: int) -> str:
        result = ""
        for word in text:
            temp = ord(word)
            if word in string.punctuation:
                result += word
                continue
            if word == "":
                result += word
                continue
            temp -= count
            if temp < 32:
                temp += 26
                result += chr(temp)
            else:
                result += chr(temp)
        return result
