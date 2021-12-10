"""We're doing it, reading CSV's baby"""
import os

from datautilities.data_utilities import pd, read_data
from calc.csv_test import cal_test_df

IN_PATH = r'C:/Users/Vintage PC/PycharmProjects/Calc_2-Refactor/datautilities/'
OUT_PATH = "C:\\Users\\Vintage PC\\PycharmProjects\\Calc_2-Refactor\\log\\"


def test_datautilities():
    """testing the data in the csv, lets go"""
    print(os.getcwd())
    for csvname in os.listdir(IN_PATH):

        column_log = ["TimeStamp", "FileName", "Record_Number", "Operation", "Result"]
        if csvname == "addition_test.csv":
            calc_add(csvname, column_log)
        elif csvname == "subtraction_test.csv":
            calc_sub(csvname, column_log)
        elif csvname == "multiplication_test.csv":
            calc_mult(csvname, column_log)
        elif csvname == "division_test.csv":
            calc_div(csvname, column_log)


def calc_add(csvname, column_log):
    """Performing addition on csv data"""
    filepath = IN_PATH + csvname
    data_util = read_data(filepath)
    operation = 'add'
    operand = '+'
    add_results_list, \
        add_calc_result, \
        final_result, newdb_list = cal_test_df(data_util, csvname, operation, operand)
    del newdb_list
    assert add_calc_result, final_result == add_calc_result
    results_df = pd.DataFrame(add_results_list, columns=column_log)
    results_out = os.path.join(OUT_PATH, csvname)
    results_df.to_csv(results_out, index=False)


def calc_sub(csvname, column_log):
    """Performing subtraction on csv data"""
    filepath = IN_PATH + csvname
    data_util = read_data(filepath)
    operation = 'subtract'
    operand = '-'
    sub_results_list, sub_calc_result, \
        final_result, newdb_list = cal_test_df(data_util, csvname, operation, operand)
    del newdb_list
    assert sub_calc_result, final_result == sub_calc_result
    results_df = pd.DataFrame(sub_results_list, columns=column_log)
    results_out = os.path.join(OUT_PATH, csvname)
    results_df.to_csv(results_out, index=False)


def calc_mult(csvname, column_log):
    """Performing multiplication on csv data"""
    filepath = IN_PATH + csvname
    data_util = read_data(filepath)
    operation = 'multiply'
    operand = '*'
    mult_results_list, mult_calc_result, \
        final_result, newdb_list = cal_test_df(data_util, csvname, operation, operand)
    del newdb_list
    assert mult_calc_result, final_result == mult_calc_result
    results_df = pd.DataFrame(mult_results_list, columns=column_log)
    results_out = os.path.join(OUT_PATH, csvname)
    results_df.to_csv(results_out, index=False)


def calc_div(csvname, column_log):
    """Performing division on csv data"""
    filepath = IN_PATH + csvname
    data_util = read_data(filepath)
    operation = 'divide'
    operand = '/'
    newdb_columns = ["Time_Stamp", "File_Name", "Record_Number", "Error"]
    operation = operation.strip()
    div_results_list, div_calc_result, \
        final_result, newdb_list = cal_test_df(data_util, csvname, operation, operand)
    assert div_calc_result, final_result == div_calc_result
    results_df = pd.DataFrame(div_results_list, columns=column_log)
    results_out = os.path.join(OUT_PATH, csvname)
    results_df.to_csv(results_out, index=False)
    newdb_list = pd.DataFrame(newdb_list, columns=newdb_columns)
    results_out_2 = os.path.join(OUT_PATH, "Divide_By_Zero_Log.csv")
    newdb_list.to_csv(results_out_2, index=False)
