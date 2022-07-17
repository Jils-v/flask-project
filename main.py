from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name = name)

app.run(debug=True)

