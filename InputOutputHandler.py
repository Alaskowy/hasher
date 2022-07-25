from typing import Union


class InputOutputHandler:
    """Class used to handle input/output from user."""

    @staticmethod
    def print(*text_list: Union[str, list]) -> None:
        """Method used to print to the user."""
        for text in text_list:
            print(text)

    @staticmethod
    def read(text: str) -> str:
        """Method used to read from user."""
        return input(text)
