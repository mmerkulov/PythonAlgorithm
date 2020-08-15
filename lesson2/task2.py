# https://app.diagrams.net/?page-id=niskdusajhPzxpmTs0UA#G1eKp2W5wpHgpv28qTq0SMU-f0MtLq0pst
# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введите число: '))
l = len(str(num))
even_number = 0
odd_number = 0
while l != 0:
    l -= 1
    z = num % 10        # последняя цифра
    if z % 2 == 0:
        even_number += 1
    else:
        odd_number += 1
    num = num // 10     # обновляем число

print(f'even_number = {even_number}', f'odd_number = {odd_number}')
