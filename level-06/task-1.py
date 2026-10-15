"""
Уровень 6, task-1: Счётчик

Пользователь вводит предложение. Программа выводит количество слов, букв и гласных.
"""

# Твой код здесь
clovo = input("приложение ")

clowa= sentence.split()
kolvo = [char for char in sentence if char.isalpha()]
glas = "аеёиоуыэюяaeiou"

da= sum(1 for char in letters if char.lower() in glas)

print("Количество слов:", len(clowa))
print("Количество букв:", len(kolvo))
print("Количество гласных:", da)
