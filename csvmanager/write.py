import os

class Write:
    @staticmethod
    def data_frame_to_csv_file(filename, df):
        return df.to_csv(os.path.abspath(filename),float_format='%.2f', index=True, header=True)
