from math import *
import numpy as np
from scipy.integrate import quad

# Функция для интегрирования
def integral(x, f, g):
    return f(x) * g(x)

# Скалярное произведение двух функций
def scalar_product(x1, x2, a, b):

    def f(x):
        return eval(x1)  

    def g(x):
        return eval(x2)  

    result, _ = quad(integral, a, b, args=(f, g))
    return result

# Пример использования:
a = float(input("Введите нижний предел интегрирования: ")) # Нижний предел интегрирования
b = float(input("Введите верхний предел интегрирования: "))  # Верхний предел интегрирования
x1 = input("Введите функцию 1: ")     # Первая функции
x2 = input("Введите функцию 2: ")     # Вторая функции

print(f'Произведение функций = {round(scalar_product(x1, x2, a, b),4)}')

