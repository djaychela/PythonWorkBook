entry_list = []
while True:
    entry = input('Enter an entry, SAVE to save, CLOSE to close: ')
    if entry == 'CLOSE':
        break
    elif entry == 'SAVE':
        file = open('ex_97.txt', 'a+')
        for entry in entry_list:
            file.writelines(entry + '\n')
        entry_list = []
        file.close()
    else:
        entry_list.append(entry)