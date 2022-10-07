"""
Module with the validator class definition.
"""

class Validator():
    def hello(self):
        print(type(self))

    def rule_for(self, item: property):
        print(isinstance(item, property))