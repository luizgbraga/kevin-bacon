import pandas as pd

class Reader:
    def __init__(self, csv_name):
        self.df = pd.read_csv(csv_name)

    def important_columns(self, columns):
        self.df.drop(self.df.columns.difference(columns), axis=1, inplace=True)
        return self

    def drop_na(self):
        self.df.dropna(inplace=True)
        return self