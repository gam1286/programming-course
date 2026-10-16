"""
Уровень 5, task-1: Калькулятор

Четыре функции: сложение, вычитание, умножение, деление. Программа спрашивает два числа и операцию, вызывает нужную функцию. Деление на ноль выдаёт сообщение, а не ошибку.
"""

# Твой код здесь

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "нол"
    return a / b


a = float(input("первое числ"))
b = float(input("второе чи сл "))

op = input("че(+, -, *, /): ")

if op == "+":
    print(plus(a, b))
elif op == "-":
    print(minus(a, b))
elif op == "*":
    print(multiply(a, b))
elif op == "/":
    print(divide(a, b))
else:
    print("хз")
