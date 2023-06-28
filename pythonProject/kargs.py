def add(*kargs):
    s = 0
    for i in kargs:
        s += i   # s = s + i
    return s

l = [2,3,4,5,6,7,8,9]
print(add(*l))