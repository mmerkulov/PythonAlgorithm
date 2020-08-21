import random

SIZE = 50
MAX_INTERVAL = 100
MIN_INTERVAL = 0

array = [random.randint(MIN_INTERVAL, MAX_INTERVAL) for i in range(SIZE)]
print(array)

max_value = 0
max_position = 0
min_value = 0
min_position = 0
for idx, value in enumerate(array):
    if max_value < value:
        max_value = value
        max_position = idx
    if min_value > value:
        min_value = value
        min_position = idx
    else:
        min_value = value
        min_position = idx

array[max_position], array[min_position] = min_value, max_value
print(array)
