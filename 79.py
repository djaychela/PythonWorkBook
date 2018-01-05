password = 'applesdA1'
password_list = list(password)
password_ok = True
if len(password)<5:
    password_ok = False
if not (any(x.isupper() for x in password)):
    password_ok = False
if not (any(x.isdigit() for x in password)):
    password_ok = False

if password_ok:
    print("Password is OK")
else:
    print("Password is NOT OK.")
