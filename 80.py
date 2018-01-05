password = 'apps'
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
else:
    print(f"Password is NOT OK")
    for reason in password_reason:
        print(reason)
