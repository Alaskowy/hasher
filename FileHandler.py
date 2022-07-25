class FileHandler:
    """Class used to file handling"""

    @staticmethod
    def save_to_file(text: str, filename: str) -> None:
        """Method used to save to file."""
        with open(filename, "w") as file:
            file.write(text)

    @staticmethod
    def read_from_file(filename: str) -> list[str]:
        """Method used to read the file."""
        try:
            with open(filename, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            print("File not found!")
