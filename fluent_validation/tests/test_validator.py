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

    def __init__(self) -> None:
        super().__init__()
        self.rule_for("name").is_none()
        print(self.rule_for("name")._rules)

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
        ...