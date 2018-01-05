import glob

file_list = glob.glob('ex_45/*.txt')
letters_list=[]

for filename in file_list:
    with open(filename,'r') as file:
        letter = file.read().strip('\n')
        if letter in 'python':
            letters_list.append(letter)

print(letters_list)
