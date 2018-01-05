countries_list = []
with open('countries-clean.txt','r') as file:
    for country in file:
        countries_list.append(country.strip('\n'))
checklist = ["Portugal", "Germany", "Munster", "Spain"]
checked = [country for country in checklist if country in countries_list]
print(checked)