# https://app.diagrams.net/?page-id=QK2SJbzOO3gyF4ZiwVJe#G1eKp2W5wpHgpv28qTq0SMU-f0MtLq0pst
# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

def show_ascii(text='', num=32, i=0):
    if num == 127:
        return text
    else:
        if i == 10:
            i = 0
            return show_ascii(text + '\n', num + 1, i + 1)
        else:
            return show_ascii(text + str(num) + '-' + chr(num) + ' ', num + 1, i + 1)
print(show_ascii())