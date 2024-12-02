from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/parents')
def parents():
    return render_template("parents.html")

@app.route('/child')
def child():
    return render_template("child.html")

@app.route('/services')
def services():
    return render_template("services.html")
