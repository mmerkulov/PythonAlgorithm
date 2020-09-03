import random

# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
#     Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

MIN_BASE = 0
MAX_BASE = 10
MIN_VAL = -100
MAX_VAL = 99


def revers_bubble_sort(array):
    n = 0
    while n <= len(array):
        for i in range(1, len(array)):
            # print(f'array[i]={array[i]}', f'array[i]={array[i - 1]}')
            if array[i] > array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
            # print(array)
        n += 1

main_array = [2, 5, 1, 3, 7, 6, 10, 8, 9]
main_array = [random.randint(MIN_VAL, MAX_VAL) for _ in range(MIN_BASE, MAX_BASE)]

print(main_array)
print('*' * 50)
revers_bubble_sort(main_array)
print('*' * 50)
print(main_array)

# ray)
# int(main_array)



