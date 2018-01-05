import sqlite3


db = sqlite3.connect('database.db')
cursor = db.cursor()
# with open('ten-more-countries.txt','r') as file:
#     for line in file.readlines():
#         cid, country, area = line.split(',')
#         print(cid, country, area)
#         if cid != 'ID':
#             cid = int(cid)
#             area = int(area)
#             cursor.execute('INSERT INTO countries (id, country, area) VALUES (?, ?, ?)',(cid, country, area))
# cursor.execute("COMMIT ")

cursor.execute("SELECT * from countries")
results = cursor.fetchall()
for result in results:
    print(result)