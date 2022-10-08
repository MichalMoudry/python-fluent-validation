"""
Module with a definition for option class for string input.
"""

from .base_options import BaseOptions

class StringOptions(BaseOptions):
    """
    String options.
    """
    def __init__(self, value: str) -> None:
        super().__init__(value)
        self._value = value

    def temp(self):
        return self