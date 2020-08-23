import random
import timeit
import cProfile

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
SIZE = 10
MAX_INTERVAL = 100
MIN_INTERVAL = 0

array_main = [random.randint(MIN_INTERVAL, MAX_INTERVAL) for i in range(SIZE)]


# Вариант 1
def option_1(size_=10):
    SIZE = size_
    MAX_INTERVAL = 100
    MIN_INTERVAL = 0

    array = [random.randint(MIN_INTERVAL, MAX_INTERVAL) for i in range(SIZE)]

    max_value = array[0]
    max_position = 0
    min_value = array[0]
    min_position = 0
    for idx, value in enumerate(array):
        if max_value < value:
            max_value = value
            max_position = idx
        if min_value > value:
            min_value = value
            min_position = idx
    array[max_position], array[min_position] = min_value, max_value

# Вариант 2
def option_2(size_=10):
    SIZE = size_
    MAX_INTERVAL = 100
    MIN_INTERVAL = 0

    array = [random.randint(MIN_INTERVAL, MAX_INTERVAL) for i in range(SIZE)]
    min_value1 = min(array)
    min_idx1 = array.index(min_value1)
    max_value1 = max(array)
    max_idx1 = array.index(max_value1)
    array[max_idx1], array[min_idx1] = min_value1, max_value1

# Вариант 3

def option_3(size_):
    SIZE = size_
    MAX_INTERVAL = 100
    MIN_INTERVAL = 0

    array = [random.randint(MIN_INTERVAL, MAX_INTERVAL) for i in range(SIZE)]
    array.sort()
    min_value2 = array[0]
    max_idx2 = len(array) - 1
    max_value2 = array[max_idx2]
    array[0] = max_value2
    array[max_idx2] = min_value2

# print('option_1')
# print(timeit.timeit('option_1(100)', number=100, globals=globals()))     # 0.0524641
# print(timeit.timeit('option_1(250)', number=100, globals=globals()))     # 0.11530390000000001
# print(timeit.timeit('option_1(500)', number=100, globals=globals()))     # 0.1822239
# print(timeit.timeit('option_1(1000)', number=100, globals=globals()))    # 0.28660149999999995
# print('option_2')
# print(timeit.timeit('option_2(100)', number=100, globals=globals()))     # 0.0420446000000001
# print(timeit.timeit('option_2(250)', number=100, globals=globals()))     # 0.06391499999999994
# print(timeit.timeit('option_2(500)', number=100, globals=globals()))     # 0.13148360000000003
# print(timeit.timeit('option_2(1000)', number=100, globals=globals()))    # 0.23264700000000005
# print('option_3')
# print(timeit.timeit('option_3(100)', number=100, globals=globals()))     # 0.028739599999999976
# print(timeit.timeit('option_3(250)', number=100, globals=globals()))     # 0.0660651000000001
# print(timeit.timeit('option_3(500)', number=100, globals=globals()))     # 0.115699
# print(timeit.timeit('option_3(1000)', number=100, globals=globals()))    # 0.2457878

# cProfile.run('option_1(1000)')   #  0.000
# cProfile.run('option_1(2500)')   #  0.001
# cProfile.run('option_1(5000)')   #  0.002
# cProfile.run('option_1(10000)')  #  0.013

# cProfile.run('option_2(1000)')      # 0.000
# cProfile.run('option_2(2500)')      # 0.000
# cProfile.run('option_2(5000)')      # 0.003
# cProfile.run('option_2(10000)')     # 0.000

cProfile.run('option_3(1000)')  # 0.000
cProfile.run('option_3(2500)')  # 0.001
cProfile.run('option_3(5000)')  # 0.000
cProfile.run('option_3(10000)') # 0.000