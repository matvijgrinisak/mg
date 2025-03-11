num1 = float(input("num1="))
num2 = float(input("num2="))
operation = input("operation=")

def calc(num1,num2,operation):
    if operation == "+":
        return num1+num2

    elif operation == "-":
        return num1 - num2

    elif operation == "*":
        return num1 * num2

    elif operation == "/":
        return num1 / num2

print(calc(num1, num2,operation))





