import sqlite3
import pandas as pd

db = sqlite3.connect('database.db')
cursor = db.cursor()
cursor.execute('SELECT * FROM countries where area > 2000000')
results = cursor.fetchall()
db.close()

df = pd.DataFrame.from_records(results)
df.columns=['Index','Country','Area','Population']
print(df.head())
df.to_csv('countries_big_area.csv', index=False)

