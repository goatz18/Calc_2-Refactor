"""Testing Addition"""
from calc.calculations.addition import Addition
import pandas as pd
data = pd.read_csv("../fileutilities/addition.csv")


def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    # Arrange
    mynumbers = (1.0, 2.0)
    addition = Addition(mynumbers)
    # Act
    # Assert
    assert addition.get_result() == 3.0
