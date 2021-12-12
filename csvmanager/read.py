import os.path

import pandas as pd


class Read:
    @staticmethod
    def read_calc_history_from_df(filepath):
        data = pd.read_csv(os.path.abspath(filepath))
        return data
