from Hasher import Hasher


class Controller:
    def __init__(self):
        self.hasher = Hasher()

    def show_menu(self):
        """Shows menu"""
        print("Welcome to Hasher! Please select one of the functions:")
        functions = {1: "Encrypt text",
                     2: "Encrypt text to file",
                     3: "Decrypt text from file",
                     4: "Show saved encrypted words"}
        for i in functions.keys():
            print(f"{i}. {functions[i]}")
        select = int(input("Please select proper function!"))
        while select is not int and select not in (1, len(functions)):
            select = int(input("Please select proper function!"))

        if select == 1:
            self.encrypt()
        if select == 2:
            self.encrypt_to_file()
        if select == 3:
            self.decrypt_from_file()
        if select == 4:
            self.show_saved_words()




    def encrypt(self) -> None:
        print("Please input text to be encrypted: ")
        text_to_encrypt = input()
        print(self.hasher.encrypt(text_to_encrypt))

    def encrypt_to_file(self) -> None:
        print("Please input text to be encrypted: ")
        text_to_encrypt = input()
        print("Please input filename: ")
        filename = input()
        self.hasher.encrypt_to_file(text_to_encrypt, filename)

    def decrypt_from_file(self) -> None:
        print("Please input filename: ")
        file_to_decrypt = input()
        self.hasher.decrypt_from_file(filename=file_to_decrypt)

    def show_saved_words(self) -> None:
        pass

