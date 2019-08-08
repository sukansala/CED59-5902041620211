from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


@app.route("/")
def index():
    return render_template('index.html')


#@app.route('/', methods=["post"])
#def register():
#    return 'xyz'


@app.route('/', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
