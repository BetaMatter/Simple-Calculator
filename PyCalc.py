import tkinter as tk


x = 0
y = 0
z = 0


def get_number():
    global x, y, z
    x = 0
    y = 0
    z = 0
    x = float(input("Enter your first number: "))
    y = float(input("Enter your second number: "))
    ask_operation()


def ask_operation():
    answer = input("What operation would you like to perform? +, -, *, /: ")
    if answer == "+":
        addition()
    elif answer == "-":
        subtraction()
    elif answer == "*":
        multiply()
    elif answer == "/":
        divide()
    else:
        print("You entered an invalid operation\n")
        ask_operation()


def addition():
    global x, y, z
    z = x + y
    return int(z)


def subtraction():
    global x, y, z
    z = x - y
    return int(z)


def multiply():
    global x, y, z
    z = x * y
    return int(z)


def divide():
    global x, y, z
    z = x / y
    return int(z)


def repeat_calc():
    get_number()


get_number()
print(z)
repeat_calc()
