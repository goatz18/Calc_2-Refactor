"""Testing Division"""
import unittest
from calc.calculations.division import Division
import pandas as pd
data = pd.read_csv("../fileutilities/division.csv")


class DivisionTest(unittest.TestCase):
    """Unit Test Class"""

    def setUp(self):
        """ self """
        self.calc = None

    def perform_division(self, my_numbers):
        """Setup function"""
        self.calc = Division(my_numbers)

    def test_calculation_division(self):
        """testing that our calculator has a static method for division"""
        # Arrange
        my_numbers = (4.0, 2.0, 0.0)
        self.perform_division(my_numbers)
        # Act
        # Assert
        assert self.calc.get_result() == 2.0
        assert self.assertRaises(ZeroDivisionError)
