import datetime

age = int(input("Enter your age: "))
year = datetime.datetime.now().year-age

print(f'You were born in {year}')