import sqlite3
import glob

print(glob.glob("*.*"))


with open('/Users/darrenjones/PycharmProjects/PythonWorkBook/ten-more-countries.txt','r') as file:
    countries = file.read()

print(countries)