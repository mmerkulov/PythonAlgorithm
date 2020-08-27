import timeit
import cProfile
import math


def sieve(n, idx):
    """Ф-ия поиска простого натурального числа через решето Эратосфена

    :param n: значение, до которого создаём массив
    :param idx: индекс простого натурального числа
    :return: простое натуральное число
    """

    # в процессе тестирования, я понял. что:
    # 1. очень медленно ищутся простые числа на больших массивах
    # 2. 99.9% нужно как-то получать значение в процессе поиска, а не в самом конце
    list_number = [x for x in range(2, n + 1)]
    i = 0

    # обработка первых значений и "некорректных"
    if idx == 1:
        return 2
    elif idx < 1:
        return 0

    for current_val in list_number:
        try:
            i = list_number.index(current_val ** 2)
        except Exception:
            i = i + 1
        for val in list_number[i:]:
            if val % current_val == 0:
                list_number.pop(list_number.index(val))

    return list_number[idx - 1]  # Так как индексация идёт с 0


def sieve_atkin(n, idx):
    """Ф-уция, определения простого числа на месте Idx в массиве N через алгоритм Аткина

    :param n: значение, до которого создаём массив
    :param idx: индекс простого натурального числа
    :return: простое натуральное число
    """

    sqrt_n = int(math.sqrt(n))
    i = int(math.sqrt((n + 1) / 2))

    for x in range(1, i):
    x2 = x ** 2

    for y in range(1, sqrt_n):
        y2 = y ** 2

        z = 3 * x2 + y2

        if z <= n and z % 12 == 7:
            print(z)

        z += x2

        if z <= n and z % 12 in (1, 5):
            print(z)

        if x > y:
            z -= x2 + 2 * y2

            if z <= n and z % 12 == 11:
                print(z)
    return 0

# cProfile.run('sieve(100)')
# print(timeit.timeit('sieve(100)', number=100, globals=globals()))   # 22.355054900000003
# print(timeit.timeit('sieve(500)', number=100, globals=globals()))   # 22.319745700000002

print(sieve_atkin(100, 5))