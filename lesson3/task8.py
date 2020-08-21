# Задача №8
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу


print('Введите значения с клавиатуры для заполнения матрицы: ')

# Заполяем массив
array = []
for i in range(1, 5):
    dirty_array = input('Введите 4-е числа через пробел: ')
    row_list = dirty_array.split()
    array.append(row_list)

# # исходная матрица
# Решение №1, работает, но не нравится
# col1 = 0
# col2 = 0
# col3 = 0
# col4 = 0
#
# for idx, val in enumerate(array):
#     for i, j in enumerate(val):
#         if i == 0:
#             col1 = col1 + int(j)
#         elif i == 1:
#             col2 = col2 + int(j)
#         elif i == 2:
#             col3 = col3 + int(j)
#         else:
#             col4 = col4 + int(j)
# result = [col1, col2, col3, col4]
#
# # добавляем 5-ую строчку
# array.append(result)
# print(array[4])

## Решение №2
# array = [[1, 2, 3, 4],
#          [1, 2, 3, 4],
#          [1, 2, 3, 4],
#          [1, 2, 3, 4]
#          ]
# print(array)
sum_col = 0
result = []
for row_idx, row in enumerate(array):
    for val_idx, val in enumerate(row):
        sum_col += int(array[val_idx][row_idx])
    result.append(sum_col)
    sum_col = 0
array.append(result)
print(array)



