def mul(*kargs):
    if len(kargs) < 2:
        return None

    r = 1
    for elem in kargs:
        r = r * elem
    return r


r = mul(2)
print(r)

r = mul(2, 3)
print(r)

r = mul(2, 3, 4)
print(r)

r = mul(2, 3, 4, 5)
print(r)

l = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
r = mul(*l)
print(r)
