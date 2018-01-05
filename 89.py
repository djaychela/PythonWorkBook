import sqlite3

db = sqlite3.connect('database.db')
cursor = db.cursor()
cursor.execute("SELECT country FROM countries WHERE area > 2000000")
results = cursor.fetchall()
db.close()
for result in results:
    print(result[0])
