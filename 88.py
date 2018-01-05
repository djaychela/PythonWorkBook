import pandas as pd

df = pd.read_csv('countries-by-area.txt', index_col='rank')
df['density']=df['population_2013']/df['area_sqkm']
df = df.sort_values(by='density', ascending=False)

for index, row in df[:5].iterrows():
    print(row['country'])
