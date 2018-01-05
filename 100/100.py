from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def rootmethod():
    errors = []
    if request.method == 'POST' and request.form.get('submit_button') == 'pressed_1':
        username = request.form.get('username')
        password = request.form.get('password')
        username_error = check_username(username)
        if username_error:
            errors.append(username_error)
        password_errors = check_password(password)
        if password_errors:
            for password_error in password_errors:
                errors.append(password_error)
        if not username_error and not password_errors:
            add_username(username)
            errors.append('Success')

    return render_template('index.html', errors=errors)


def check_username(username):
    with open('100_users.txt','r') as file:
        usernames = file.read().split('\n')
    if username in usernames:
        return "That username is already in use"

def add_username(username):
    with open('100_users.txt','a+') as file:
        file.write(username + '\n')


def check_password(password):
    password_reason=[]
    if len(password)<5:
        password_reason.append('Too short.')
    if not (any(x.isupper() for x in password)):
        password_reason.append('No capitals.')
    if not (any(x.isdigit() for x in password)):
        password_reason.append('No numbers.')
    return password_reason



app.run()