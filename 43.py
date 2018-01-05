from string import ascii_lowercase

with open('ex_43.txt','w') as file:
    for i in range(0, len(ascii_lowercase), 2):
        file.write(ascii_lowercase[i:i+2]+'\n')
        