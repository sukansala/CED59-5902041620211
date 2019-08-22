from flask import Flask, render_template, request
from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'


class Form(FlaskForm):
    fname = StringField("fname", validators=[InputRequired()])
    lname = StringField("lanme", validators=[InputRequired()])
    email = StringField("email", [InputRequired(""), Email("Please enter email is ______@gmail.com")])
    username = StringField("username", validators=[InputRequired()])
    password = PasswordField("password",
                             validators=[InputRequired(), Length(min=8, message="Please enter password as size")])


@app.route('/')
def SingUp():
    form = Form()
    return render_template('index.html', form=form)


@app.route('/register', methods=["post"])
def register():
    username = request.form['username']
    form = Form()
    if form.validate_on_submit():
        return "Index Page!! Welcome your are " + username
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
