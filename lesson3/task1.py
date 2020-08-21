#

array = [i for i in range(2, 100)]
array1 = [i for i in range(2, 10)]

print(array)
print(array1)
amount = 0
for i in array1:
    for j in array:
        if j % i == 0:
          amount += 1
    print(f'{i} => {amount} раз')
    amount = 0
