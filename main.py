from flask import Flask, render_template, url_for, request
from math import sqrt
from flask_sqlalchemy import SQLAlchemy

def floater(num1, num2):
    if num1 < 0 and num2 < 0:
        num1 *= 10
        num2 *= 10

def answerdei(title, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    if title == "+":
        return str(num1 + num2)
    elif title == "+f":
        return str((num1 * 10 + num2 * 10))
    elif title == "-":
        return str(num1 - num2)
    elif title == "*":
        return str(num1 * num2)
    elif title == "/":
        return str(num1 / num2)
    elif title == "//":
        return str(num1 // num2)
    elif title == "%":
        return str(num1 % num2)
    elif title == "sqrt":
        return str(sqrt(num1))
    elif title == "**":
        return str(num1 ** num2)
    if num1 < 0 and num2 < 0:
        num1 /= 100
        num2 /= 100
app = Flask(__name__)

num1= 100
num2 = 200
title = "+"
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/calculator", methods=['POST', 'GET'])
def calculator():
    global num1
    global num2
    global title
    if request.method == 'POST':
        num1 = request.form['title']
        title = request.form['sign']
        num2 = request.form['text']
        return render_template("calculator.html", answer = answerdei(title, num1, num2))
    else:
        return render_template("calculator.html")

@app.route("/answer")
def answer():
    return render_template("/answer.html", answer = answerdei(title, num1, num2))



@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)