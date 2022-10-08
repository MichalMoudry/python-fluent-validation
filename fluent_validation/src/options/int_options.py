"""
Module with a definition for option class for int input.
"""

from .base_options import BaseOptions

class IntOptions(BaseOptions):
    """
    Integer options.
    """
    def __init__(self, value: int) -> None:
        super().__init__(value)
        self._value = value

    def temp2(self):
        return self