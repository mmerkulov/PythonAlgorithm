# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

def func_hex_to_dec(num):
    """Ф-ция перевода 16-ти ричного числа в 10-тичное

    :param num: список состоящий из элементов 16-тиричного числа
    :return: 10-тичное число
    """
    sum = 0
    power = len(num) - 1

    for x in num:
        sum = sum + base.get(x) * (16 ** power)
        # print(f'base.get(x)={base.get(x)}')
        # print(f'sum={sum}')
        power -= 1
    return sum


def func_dec_to_hex(num):
    if num < 10:
        return num
    elif num < 16:
        return list(base.keys())[list(base.values()).index(num)]

    answer = ''

    while num > 16:

        a = num // 16  # делим на цело и запоминаем целое
        b = num % 16  # делим и получаем остаток от деления
        if b < 16:
            if b > 9:
                b = list(base.keys())[list(base.values()).index(b)]  # находим Ключ в словаре по Значению
            answer += str(b)

        if a < 16:
            if a > 9:
                a = list(base.keys())[list(base.values()).index(a)]
            answer += str(a)

        num = a

    return answer[::-1]


base = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
a = input('Введите первое число: ')
b = input('Введите второе число: ')
num1 = []
num2 = []

for char in a:
    num1.append(char)

for char in b:
    num2.append(char)

print(func_dec_to_hex(func_hex_to_dec(num1) + func_hex_to_dec(num2)))
print(func_dec_to_hex(func_hex_to_dec(num1) * func_hex_to_dec(num2)))

