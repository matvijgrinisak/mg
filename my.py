

while True:
    num1 = float(input("num1= "))
    num2 = float(input("num2= "))
    operation = input("operation= ")

    def calc(num1, num2, operation):
        if operation == "+":
           return num1 + num2
        elif operation == "-":
           return num1 - num2
        elif operation == "*":
           return num1 * num2
        elif operation == "/":
           return num1 / num2
        else:
            print("Error")

print(calc(num1, num2,operation))

if operation == "0":
    print("Error")


