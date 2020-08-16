import random

SIZE = 10
MAX_INTERVAL = 100
MIN_INTERVAL = 0

array = [random.randint(MIN_INTERVAL, MAX_INTERVAL) for i in range(SIZE)]
print(array)

result = []

for idx, value in enumerate(array):
    if value % 2 == 0:
        result.append(idx)

print(result)
