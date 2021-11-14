"""Division Class"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        div_result = 1.0
        for value in self.values:
            div_result = div_result * value
        return div_result
