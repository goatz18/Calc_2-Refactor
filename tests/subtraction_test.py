"""Testing Subtraction"""
from calc.calculations.subtraction import Subtraction
import pandas as pd
data = pd.read_csv("../fileutilities/subtraction.csv")


def test_calculation_subtraction():
    """testing that our calculator has a static method for subtraction"""
    # Arrange
    mynumbers = (1.0, 2.0)
    subtraction = Subtraction(mynumbers)
    # Act
    # Assert
    assert subtraction.get_result() == -3
