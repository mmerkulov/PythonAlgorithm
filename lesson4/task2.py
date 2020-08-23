import timeit
import cProfile


def sieve(idx):
    """Ф-ия поиска простого натурального числа через решето Эратосфена

    :param idx: индекс простого натурального числа
    :return: простое натуральное число
    """

    list_number = [x for x in range(2, 10001)]
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

def prime(idx):

    return 0


# cProfile.run('sieve(100)')
# print(timeit.timeit('sieve(100)', number=100, globals=globals()))   # 22.355054900000003
# print(timeit.timeit('sieve(500)', number=100, globals=globals()))   # 22.319745700000002

