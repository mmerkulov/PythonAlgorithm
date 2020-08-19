
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу


print('Введите значения с клавиатуры для заполнения матрицы: ')

# Заполяем массив
# array = []
# for i in range(1, 5):
#     dirty_array = input('Введите 4-е числа через пробел: ')
#     row_list = dirty_array.split()
#     array.append(row_list)
#
# # исходная матрица
# print(array)
# Решение в лоб, которое мне не нравится, не универсальное совсем

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


array = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], []]
print(array)

for row_idx, row in enumerate(array):
    # print(row)
    for idx, val in enumerate(row):
        array[4][0] = [array[4][0] + int(val) if idx == 0 else 0]
        array[4][1] = [array[4][1] + int(val) if idx == 1 else 0]

print(array[3][0])