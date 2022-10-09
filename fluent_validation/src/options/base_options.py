"""
Module with a definition for base options class.
"""

def is_none(value) -> bool:
    return value == None

def is_not_none(value) -> bool:
    return value != None

rules = {
    "is_none": (is_none, "Evaluated value is not none."),
    "is_not_none": (is_not_none, "Evaluated value is none.")
}

class BaseOptions():
    """
    Base options class for a evaluated property.
    """
    _rules = {}

    def __init__(self, value) -> None:
        self._value = value

    def is_none(self):
        self._rules[f"{self._value}_is_none"] = rules["is_none"]
        return self
    
    def is_not_none(self):
        self._rules[f"{self._value}_is_not_none"] = rules["is_not_none"]
        return self