import pandas as pd

class Read:
    @staticmethod
    def read_calc_history_from_df(filename):
        data = pd.read_csv(filename)
        calc_history_df = pd.DataFrame(data, columns=['value1', 'value2', 'operator', 'result'])
        return calc_history_df
