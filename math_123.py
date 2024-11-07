from math import sqrt

def answerget(title, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    if title == "+":
        return str(num1 + num2)
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
    elif title == "Линейное уравнение":
        return str(-num1 / num2)
    elif title == "**":
        return str(num1 ** num2)