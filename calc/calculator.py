""" This is the increment function"""

from calc.history.calculations import Calculations


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def get_last_calc_value():
        """ This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        return Calculations.get_last_calculation_result_value()

    @staticmethod
    # tuple allows me to pass in as many values as a I want
    def addition(tuple_values: tuple):
        """ adds list of numbers"""
        Calculations.add_addition_calculation(tuple_values)
        return True

    @staticmethod
    def subtraction(tuple_values: tuple):
        """ subtract a list of numbers from result"""
        Calculations.add_subtraction_calculation(tuple_values)
        return True

    @staticmethod
    def multiplication(tuple_values: tuple):
        """ multiplication number from result"""
        Calculations.add_multiplication_calculation(tuple_values)
        return True

    @staticmethod
    def division(tuple_values: tuple):
        """ divide_numbers  from result"""
        Calculations.add_division_calculation(tuple_values)
        return True

    @staticmethod
    def get_history():
        """ Get history """
        return Calculations.history

    @staticmethod
    def get_history_from_csv():
        """ Get history """
        return Calculations.read_history_from_csv()

    @staticmethod
    def write_history_to_csv():
        """ Get history """
        return Calculations.write_history_to_csv()
    