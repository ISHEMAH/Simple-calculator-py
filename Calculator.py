num1 = input("Enter the first number :\n")
number1 = int(num1)
operator = input("Enter operator :\n")
num2 = input("Enter the second number :\n")
number2 = int(num2)


def calculator(digit1, digit2, operation):
    if operation == "+":
        return digit1 + digit2
    elif operation == "-":
        return digit1 - digit2
    elif operation == "*":
        return digit1 * digit2
    elif operation == "/":
        return digit1 / digit2

print(num1 +" "+ operator +" "+ num2 + " = " + str(calculator(number1,number2,operator)))