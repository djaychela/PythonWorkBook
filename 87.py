countries_missing=[]
with open('countries-missing.txt','r') as file:
    for country in file:
        countries_missing.append(country.strip('\n'))
missing=['Germany','Portugal','Spain']
for missed in missing:
    countries_missing.append(missed)
countries_missing.sort()

print(countries_missing)