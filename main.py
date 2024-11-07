from flask import Flask, render_template, url_for, request
from math import sqrt
from flask_sqlalchemy import SQLAlchemy
from math_123 import answerget

def floater(num1, num2):
    if num1 < 0 and num2 < 0:
        num1 *= 10
        num2 *= 10


app = Flask(__name__)

num1= 100
num2 = 200
title = "+"
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/calculator", methods=['POST', 'GET'])
def calculator():
    if request.method == 'POST':
        num1 = request.form['title']
        title = request.form['sign']
        num2 = request.form['text']
        return render_template("calculator.html", answer = answerget(title, num1, num2))
    else:
        return render_template("calculator.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)