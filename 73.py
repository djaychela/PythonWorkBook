import pandas as pd

df = pd.read_csv('http://www.pythonhow.com/data/sampledata.txt')
df2 = df*2
df2.to_csv('ex_73.csv', index=False)