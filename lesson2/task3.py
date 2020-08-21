# https://app.diagrams.net/?page-id=4pcr6fxJhgjnMUNqEWlp#G1eKp2W5wpHgpv28qTq0SMU-f0MtLq0pst
# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

num = int(input('Введите число: '))
l = len(str(num))
s = ''
while l != 0:
    l -= 1
    z = num % 10
    s += str(z)
    num = num // 10
print(s)
