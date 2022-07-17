from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name = name)

app.run(debug=True)

