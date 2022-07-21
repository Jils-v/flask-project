from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form, FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'

bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField("What is your name ?", validators=[InputRequired()])
    submit = SubmitField("submit")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/", methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form = form, name = name)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name = name)

app.run(debug=True)

