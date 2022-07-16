from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    hello = 'hello world'
    return render_template('index.html', hello = hello)

app.run(debug=True)

