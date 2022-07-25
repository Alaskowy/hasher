from buffer import Buffer
from InputOutputHandler import InputOutputHandler as io
from typing import Union, Callable
from json_converter import JsonConverter
from FileHandler import FileHandler as fh
from rot import Rot, Rot47, Rot13
from EncryptedText import EncryptedText


class Manager:
    """Main class to take care of the program"""

    def __init__(self):
        self.is_running = True
        self.buffer = Buffer()
        self.functions: dict[str, Callable] = {
            "1": self.encrypt_text,
            "2": self.save_buffer,
            "3": self.decrypt_text,
            "4": self.peak_buffer,
            "5": self.load_from_file,
            "6": self.end_app,
        }

    def run(self):
        """Method to run the app"""
        while self.is_running:
            self.show_menu()
            user_instruction = io.read("")
            self.handle_instruction(user_instruction)
            io.print("\n")

    def encrypt_text(self) -> None:
        """Method to encrypt text"""
        rot: Rot = self.get_encryptor()
        print("Please input text to encode: ")
        data = io.read("Input: ")
        encoded_text: str = rot.encode(data)
        encrypted_text: EncryptedText = EncryptedText(rot.rot_type(), encoded_text)
        self.buffer.add(encrypted_text)

    def save_buffer(self, filename: None) -> None:
        """Method to save encrypted words in buffer to file"""
        if not filename:
            filename: str = io.read("Provide filename: ")
        text: str = self.buffer_2_json()
        fh.save_to_file(text=text, filename=filename)
        io.print(f"Saved to file '{filename}'.")

    def decrypt_text(self) -> None:
        """Method to take the text to decrypt from user and returned decrypted text"""
        print("Please input text to decode: ")
        data = io.read(text="Input: ")
        if self.rot_choice:
            io.print(self.rot13.decode(data))
        else:
            io.print(self.rot47.decode(data))

    def end_app(self) -> None:
        self.is_running = False

    def show_menu(self):
        """Shows menu"""
        io.print("Welcome to Hasher! Please select one of the functions:")
        io.print(
            "1. Encrypt text",
            "2. Save buffer",
            "3. Decrypt text",
            "4. Show saved encrypted words",
            "5. Load from file",
            "6. End app",
        )

    def handle_instruction(self, user_txt: Union[str, int]):
        """Method to handle user instructions and check if the instruction exist"""
        if user_txt in self.functions:
            self.functions.get(user_txt)()
        else:
            io.print(f"{user_txt} is not a instruction")

    def buffer_2_json(self):
        """Method to parse buffer to json"""
        return JsonConverter.obj_to_json([obj.to_dict() for obj in self.buffer.peak()])

    def peak_buffer(self) -> None:
        """Method to show buffer"""
        io.print("This is content of the buffer: ")
        if isinstance(self.buffer.peak(), list):
            io.print(self.buffer.peak())
        else:
            io.print(self.buffer_2_json())

    def get_encryptor(self) -> Rot:
        """Method to get the encryptor from the user"""
        io.print(
            "Which encryptor do you want to use?",
            "Pick the number.",
            "1. ROT47",
            "2. ROT13",
        )
        encryptor_no = io.read("")
        if encryptor_no == "1":
            return Rot47()
        elif encryptor_no == "2":
            return Rot13()
        else:
            io.print("This is not valid answer.")
            return self.get_encryptor()

    def load_from_file(self) -> None:
        """Method to load data from file, then add the data to buffer."""
        filename: str = io.read("Provide filename: ")
        data = fh.read_from_file(filename)
        string = ""
        for row in data:
            string += row
        converted = JsonConverter.json_to_obj(string)
        self.buffer.add(converted)
