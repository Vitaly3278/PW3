# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


def fibonacci(n):
    fibo = []
    a, b = 1, 1
    for i in range(n):
        fibo.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n + 1):
        fibo.insert(0, a)
        a, b = b, a - b
    return fibo


n = int(input('Введите число: '))

print(fibonacci(n))
