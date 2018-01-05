from flask import Flask, request, render_template

app = Flask(__name__)

entries=[]


@app.route('/', methods=['GET', 'POST'])
def rootmethod():
    global entries
    if request.method == 'POST' and request.form.get('submit_button') == 'pressed_1':
        entry_text = request.form.get('entry_text')
        entries.append(entry_text)

    if request.method == 'POST' and request.form.get('submit_button') == 'pressed_2':
        entry_text = request.form.get('entry_text')
        entries.append(entry_text)
        with open('ex_99.txt','a+') as file:
            for entry in entries:
                file.write(entry + '\n')
        entries = []

    return render_template('index.html', entries=entries)


app.run()