"""Read csv data from file"""
import pandas as pd


def read_data(data_path):
    """Read csv data from file"""
    data= pd.read_csv(data_path)
    data_frame = pd.DataFrame(data, columns=['value_a', 'value_b', 'result'])
    return data_frame
