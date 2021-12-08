"""Using fancy CSV values to test the calc"""
import time
from calc.calculator import Calculator


def cal_test_df(dataframe, filename, operation, operand):
    """Function that gets data from csv and tests it in the calc"""
    results_list = []
    newdb_list = []
    for column_number in range(len(dataframe)):

        first_value = dataframe.iat[column_number, 0]
        second_value = dataframe.iat[column_number, 1]
        final_result = dataframe.iat[column_number, 3]
        unix_time_stamp = int(time.time())
        my_tuple = (first_value, second_value, final_result)
        if operation == 'add':
            Calculator.add_numbers(my_tuple)
        elif operation == 'subtract':
            Calculator.subtract_numbers(my_tuple)
        elif operation == 'multiply':
            Calculator.multiply_numbers(my_tuple)
        elif operation == 'divide':
            if second_value == 0:
                zero_error = "Divide By Zero"
                newdb_list.append((unix_time_stamp, filename, column_number, zero_error))
            else:
                Calculator.divide_numbers(my_tuple)
        calc_result = Calculator.get_last_calc_value()
        results_list.append([unix_time_stamp, filename, column_number, operand, calc_result])
    return results_list, calc_result, final_result, newdb_list
