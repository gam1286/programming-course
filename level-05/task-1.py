"""
Уровень 5, task-1: Калькулятор

Четыре функции: сложение, вычитание, умножение, деление. Программа спрашивает два числа и операцию, вызывает нужную функцию. Деление на ноль выдаёт сообщение, а не ошибку.
"""

# Твой код здесь

def pluse(a, b):
    return a + b

def minuse(a, b):
    return a - b

def umnaze(a, b):
    return a * b

def dilit(a, b):
    if b == 0:
        return "нол"
    return a / b


a = float(input("первое числ"))
b = float(input("второе чи сл "))

op = input("че(+, -, *, /): ")

if op == "+":
    print(pluse(a, b))
elif op == "-":
    print(minuse(a, b))
elif op == "*":
    print(umnaze(a, b))
elif op == "/":
    print(dilit(a, b))
else:
    print("хз")
