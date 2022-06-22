class Hasher:
    """Class used to hash text"""
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def encrypt(self, text: str) -> str:
        """Method used to hash text
        :param text: text to be hashed """
        text = text.lower()

        result = ''

        for char in text:
            if char.isalpha():
                result += self.alphabet[(self.alphabet.index(char) + 13) % 26]
            else:
                result += char

        return result
