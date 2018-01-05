from string import ascii_lowercase

with open('ex_41.txt','w') as file:
    for letter in ascii_lowercase:
        file.write(letter + '\n')

