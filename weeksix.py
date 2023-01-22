def calculator(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op =="-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return "Enter valid operator"


number1 = float(input("Enter first number"))
number2 = float(input("Enter second number"))
operator = input("Enter operator")

print(calculator(number1, number2, operator))