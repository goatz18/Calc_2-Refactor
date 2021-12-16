import pandas as pd
import os.path
from flask import render_template, request, flash, redirect, url_for, session
from datautilities.absolutepath import absolutepath

class Write:
    @staticmethod
    def write_new_calc_to_history_df(filepath, result):
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']
        data = {'Value1': [value1], 'Value2': [value2], 'Operation': [operation], 'Result': [result]}
        df = pd.DataFrame(data)
        new_calc_history_df = df.to_csv(os.path.abspath(filepath), mode='a', float_format='%.2f', index=False, header=False)
        return new_calc_history_df
