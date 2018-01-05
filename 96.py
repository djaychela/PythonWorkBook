with open('ex_96.txt', 'a+') as file:
    while True:
        value = input("Enter a Value: ")
        if value == 'CLOSE':
            break
        else:
            file.writelines(value + '\n')