from flask import Flask, render_template, url_for, request
from math import sqrt
from flask_sqlalchemy import SQLAlchemy


def answerdei(title, num1, num2):
    if title == "+":
        return str(num1 + num2)
    elif title == "-":
        return (num1 - num2)
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
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/calculator", methods=['POST', 'GET'])
def calculator():
    if request.method == 'POST':
        num1 = request.form['title']
        title = request.form['sign']
        num2 = request.form['text']
        num1 = float(num1)
        num2 = float(num2)
        return answerdei(title, num1, num2)



    else:
        return render_template("calculator.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)