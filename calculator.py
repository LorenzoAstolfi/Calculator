from art import logo
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

verify = True
while verify:
    print(logo)

    F_Num = float(input("What's the first number: "))
    oper = input("+\n-\n*\n/\nPick an operation: ")
    S_Num = float(input("What's the second number: "))
    Result = operation[oper](n1 = F_Num, n2 = S_Num)
    print(f"{F_Num} {oper} {S_Num} = {Result}")
    while input(f"Type 'y' to continue calculating with {Result}, or type 'n' to start a new calculation: ").lower() == "y":
        oper = input("+\n-\n*\n/\nPick an operation: ")
        F_Num = float(input("What's the successive number: "))
        print(f"{Result} {oper} {F_Num} = {operation[oper](n1 = F_Num, n2 = S_Num)}")
        Result = operation[oper](n1 = F_Num, n2 = S_Num)
    os.system('cls||clear')
