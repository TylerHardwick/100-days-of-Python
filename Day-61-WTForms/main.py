from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key = "runescape34orf739ff2"
Bootstrap(app)


correct_email = "admin@email.com"
correct_password = "12345678"






class MyForm(FlaskForm):
    email = EmailField(label="Email", validators=[Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == correct_email and form.password.data == correct_password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)




if __name__ == '__main__':
    app.run(debug=True)