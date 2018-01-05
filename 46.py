import os

files = os.listdir('ex_45/')
files.sort()

letter_list = []
for filename in files:
    with open('ex_45/'+filename,'r') as file:
        letter_list.append(file.read().strip('\n'))

print(letter_list)
