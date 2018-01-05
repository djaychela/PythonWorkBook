entries = []
try:
    with open('ex_95.txt') as file:
        for entry in file.readlines():
            entries.append(entry.strip('\n'))
except FileNotFoundError:
    pass

new_entries = input('Enter some comma-separated values: ')
entry_list = new_entries.split(',')
for new_entry in entry_list:
    entries.append(new_entry.strip())
print(entries)
with open('ex_95.txt','w') as file:
    for entry in entries:
        file.writelines(entry + '\n')
