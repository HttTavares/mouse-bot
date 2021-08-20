import pandas as pd

file = pd.read_csv('DataSchoemann2017.csv', sep = ';')
def create_test_csv():
    df = pd.DataFrame()
    for i in range(100):
        df = df.append(file.iloc[i*1000])
    df.to_csv('teste.csv')
