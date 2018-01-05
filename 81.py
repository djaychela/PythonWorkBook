def set_username():
    with open('81_users.txt','r') as file:
        usernames = file.read().split('\n')
    username_set = False
    while not username_set:
        username = input('Enter your username: ')
        if username in usernames:
            print("That username is already in use")
        else:
            username_set = True
    return username


def set_password():
    password_set = False
    while not password_set:
        password = input("Enter your Password: ")
        password_ok = True
        password_reason=[]
        if len(password)<5:
            password_ok = False
            password_reason.append('Too short.')
        if not (any(x.isupper() for x in password)):
            password_ok = False
            password_reason.append('No capitals.')
        if not (any(x.isdigit() for x in password)):
            password_ok = False
            password_reason.append('No numbers.')
        if password_ok:
            print("Password is OK")
            password_set = True
        else:
            print(f"Password is NOT OK")
            for reason in password_reason:
                print(reason)
    return password

user = set_username()
pword = set_password()
