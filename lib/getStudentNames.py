import pandas as pd


def getStudentNames(csv_path, column_name):
    df = pd.read_csv(csv_path)
    names = df[column_name].values
    return names
