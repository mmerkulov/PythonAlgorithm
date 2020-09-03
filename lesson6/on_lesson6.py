import sys

a = 42
b = 'Hello world'


# print(id(a))
# print(sys.getsizeof(a))

def show(x):
    print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key)
                show(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)


# show(42)
# show(a)
c = [i for i in range(11)]
print(c)
show(c)
# show(b)
# show(c)
# t = tuple(c)
# show(t)
