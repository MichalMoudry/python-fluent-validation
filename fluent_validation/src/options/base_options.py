"""
Module with a definition for base options class.
"""

class BaseOptions():
    """
    Base options class for a evaluated property.
    """
    def __init__(self, value) -> None:
        self._value = value

    def is_none(self) -> bool:
        return self._value == None
    
    def is_not_none(self) -> bool:
        return self._value != None