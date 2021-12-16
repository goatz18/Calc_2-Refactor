import os.path

import pandas as pd


class Read:
    @staticmethod
    def read_calc_history_from_df(filepath):
        data = pd.read_csv(os.path.abspath(filepath))
        data_frame = pd.DataFrame(data, columns=['value_a', 'operator', 'value_b', 'result'])
        return data_frame

