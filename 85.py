countries_output=''
with open('countries-raw.txt','r') as file:
    for current in file:
        if current != 'Top of Page\n' and current != '\n' and len(current)>3:
            countries_output+=current
print(countries_output)