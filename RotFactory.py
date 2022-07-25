from typing import Union
from rot import Rot13, Rot47


class RotFactory:
    @classmethod
    def get_rot(cls, shift: str) -> Union[Rot13, Rot47]:
        if shift == "47":
            return Rot47()
        elif shift == "13":
            return Rot13()
