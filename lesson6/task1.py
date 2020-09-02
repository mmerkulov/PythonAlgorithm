from functools import reduce
import random
import sys
import re


# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

# Вариант №1
def my_func1(array):
    result_min = 0
    result_idx = 0
    for y, x in enumerate(array):
        if x < 0:
            result_min = x  # определяем min значение, в случае если в списке может быть в 0-ом индексе положительное число
            result_idx = y
            break

    for idx, num in enumerate(array):
        if num > result_min and num < 0:
            result_min = num
            result_idx = idx

    for key, val in locals().items():
        show_film(val, key)

    return f'my_func1. Минимальное значение массива = {result_min} и находится на месте = {result_idx}.'


# Вариант №2
def my_func2(array):
    min_val = min(array)
    i = array.index(min_val)

    for idx, val in enumerate(array):
        if 0 > val > min_val:
            min_val = val
            i = idx

    for key, val in locals().items():
        show_film(val, key)

    return f'my_func2. Минимальное значение массива = {min_val} и находится на месте = {i}.'


# Вариант №3, взял с урока
def my_func3(array):
    i = 0
    idx = -1
    while i < len(array):
        if array[i] < 0 and idx == -1:
            idx = i
        elif 0 > array[i] > array[idx]:
            idx = i
        i += 1

    for key, val in locals().items():
        show_film(val, key)

    if idx != 0:
        return f'my_func3. Максимальное отрицательное значение = {array[idx]} находится на месте {idx}'
    else:
        return 'Something wrong!'


def show_film(x, y=None):
    global TOTAL_MEM
    # print(f'var_type={type(x)}, var_size={sys.getsizeof(x)}, var_name={x if y is None else y}')
    TOTAL_MEM += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_film(key)
                show_film(value)
        elif not isinstance(x, str):
            for item in x:
                show_film(item)


TOTAL_MEM = 0
MIN_BASE = 0
MAX_BASE = 20
MIN_VAL = -100
MAX_VAL = -1

array = [random.randrange(MIN_VAL, MAX_VAL) for _ in range(MIN_BASE, MAX_BASE)]
print(array)

print(my_func1(array), f'total_mem = {TOTAL_MEM}')
TOTAL_MEM = 0
print(my_func2(array), f'total_mem = {TOTAL_MEM}')
TOTAL_MEM = 0
print(my_func3(array), f'total_mem = {TOTAL_MEM}')
