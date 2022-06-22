class Hasher:
    """Class used to hash text"""
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def encrypt(self, text: str) -> str:
        """Method used to hash text
        :parameter text: text to be hashed """
        text = text.lower()

        result = ''

        for char in text:
            if char.isalpha():
                result += self.alphabet[(self.alphabet.index(char) + 13) % 26]
            else:
                result += char

        return result

    def encrypt_to_file(self, text: str, filename: str) -> None:
        """Method used to encrypt to file
        :param text: text to be hashed
        :param filename: file name of the file
        """
        with open(filename, "w") as file:
            file.writelines(self.encrypt(text))
