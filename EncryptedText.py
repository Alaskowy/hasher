from rot import Rot
from RotFactory import RotFactory


class EncryptedText:
    """Class that's handling the encrypted words"""

    def __init__(self, rot: str, text: str):
        self.__rot = rot
        self.__text = text

    def to_dict(self) -> dict:
        """Method that returns dict version of the encrypted text."""
        return {"rot": self.__rot, "text": self.__text}

    @property
    def rot(self):
        return self.__rot

    @property
    def text(self):
        return self.__text

    @classmethod
    def create(cls, data: dict):
        rot: Rot = RotFactory.get_rot(data["rot"])
        return EncryptedText(rot.rot_type(), data["text"])
