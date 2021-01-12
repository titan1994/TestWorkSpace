from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super key'


@app.route('/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')

        print(username, password)

        if username == 'root' and password == 'pass':
            message = "Correct username and password"
        else:
            message = "Wrong username or password"

    return render_template('index.html', message=message)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
