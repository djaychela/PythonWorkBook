from string import ascii_lowercase

for letter in ascii_lowercase:
    filename = 'ex_45/'+letter+'.txt'
    with open(filename, 'w') as file:
        file.write(letter)
        