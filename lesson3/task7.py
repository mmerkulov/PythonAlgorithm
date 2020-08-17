import random

# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.


SIZE = 10
MIN_INTERVAL = 0
MAX_INTERVAL = 100

array = [random.randint(MIN_INTERVAL, MAX_INTERVAL) for _ in range(SIZE)]

a = array[0]
b = array[1]
c = 0
print(array)

if a > b:
    c = b   # запоминаем, что 'a' это меньшее среди 'a' и 'b'
    b = a
    a = c

for val in array[2:]:
    if val < a:
        d = a
        b = d
        a = val
    elif val < b:
        b = val

print(a, b)

# проверям визуально, что первый и второй элемент равны min-ным
array.sort()
print(array)
