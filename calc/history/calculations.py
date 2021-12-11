"""Calculation history Class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division


class Calculations:
    """ Calculations"""
    history = []
    # pylint: disable=too-few-public-methods

    @staticmethod
    def read_history_from_csv():
        """Read the history from csv and put it into the history """
    @staticmethod

    def write_history_to_csv():
        """Write the history to csv file"""
    # pylint: disable=too-few-public-methods

    @staticmethod
    def clear_history():
        """ clear_history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """ count_history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation():
        """get_last_calculation """
        return Calculations.history[-1]

    @staticmethod
    def get_first_calculation():
        """ get_first_calculation"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)

    @staticmethod
    def get_last_calculation_result_value():
        """get last calculation"""
        calculation = Calculations.get_last_calculation()
        return calculation.get_result()

    @staticmethod
    def add_addition_calculation(values):
        """create an addition and add object to history using factory method create"""
        Calculations.add_calculation(Addition.create(values))
        # Get the result of the calculation
        return True

    @staticmethod
    def add_subtraction_calculation(values):
        """create a subtraction object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation(values):
        """create a subtraction object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return True

    @staticmethod
    def add_division_calculation(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Division.create(values))
        return True
