﻿from flask import Flask, render_template
from waitress import serve


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
