"""
Test for Validator class.
"""

import unittest
from src.validator import Validator

class TestClass(Validator):
    """
    Class used for testing validator.
    """
    _name = ""

    @property
    def name(self):
        """
        Test property 'name'.
        """
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        """
        Test property setter.
        """
        self._name = value

class ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        """
        Method for setting up a test fixture.
        """
        self.test_class = TestClass()
        return super().setUp()

    def test(self) -> None:
        print(self.test_class.rule_for(self.test_class.name).is_none())