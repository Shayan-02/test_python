num1 = int(input("enter number1: "))
op = input("enter an operator: ")
num2 = int(input("enter number2: "))

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Can't devide by zero!")
else:
    print(f"{op} is invalid")