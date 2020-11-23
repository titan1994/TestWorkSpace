from flask import Flask, render_template, request, redirect, url_for, flash
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super key'
manager = Manager(app)


@app.route('/')
@app.route('/index')
def index():
    return 'Hello'
    # user = {'username': 'линда'}
    # return render_template('index.html', title='Home', user=user)


@app.route('/login/', methods=['post', 'get'])
def login():
    message = 'Hi'
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')

        if username == 'root' and password == 'pass':
            message = "Correct username and password"
        else:
            message = "Wrong username or password"

    return render_template('login.html', message=message)


class ContactForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/contact/', methods=['get', 'post'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(name)
        print(email)
        print(message)
        # здесь логика базы данных
        print("\nData received. Now redirecting ...")
        flash('saved', "success")
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)


if __name__ == "__main__":
    # manager.run()
    app.run()
