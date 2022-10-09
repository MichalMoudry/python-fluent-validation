"""
Module with the validator class definition.
"""

from .options import *

class Validator():
    """
    Base class for outside validators.
    """
    def rule_for(self, item):
        typeof = type(item)
        if typeof == str:
            return StringOptions(item)
        elif typeof == int:
            return IntOptions(item)
        else:
            return None