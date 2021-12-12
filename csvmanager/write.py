import pandas as pd
from flask import render_template, request, flash, redirect, url_for, session
from datautilities.absolutepath import absolutepath

class Write:
    @staticmethod
    def write_new_calc_to_history_df(filepath, result):
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']
        df = pd.DataFrame(columns= [value1, value2, operation, result])
        new_calc_history_df = df.to_csv(filepath, mode='a', float_format='%.2f', index=True, header=True)
        return new_calc_history_df
