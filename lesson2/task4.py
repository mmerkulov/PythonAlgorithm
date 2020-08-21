# https://app.diagrams.net/?page-id=_ntfaa3PA2ggRSIUykr3#G1eKp2W5wpHgpv28qTq0SMU-f0MtLq0pst
# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Вветие число: '))
x = 1
z = x
while n != 1:
    x = x * -1 / 2
    z += x
    n -= 1
    print(x)
print(f'Сумма ряда = {z}')

## recursive

def my_func(num, n):
    n -= 1
    if n == 0:
        return num
    else:
        return num + my_func(num * -1 / 2, n)

print(my_func(1, 4))