def str_add(f):
    def inner(x, y):
        int_x = int(x)
        int_y = int(y)
        s = f(int_x, int_y)
        return s
    return inner


@str_add
def add(a, b):
    return a + b


print(add(2, 3))
print(add('123', '120'))
