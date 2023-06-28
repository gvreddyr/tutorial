
def add(aa, bb=0, cc=12):
    print("aa: ", aa)
    print("bb: ", bb)
    print("cc: ", cc)

    s = aa + bb + cc
    return s

def sub(a,b):
    dif = a - b
    return dif

def mul(a,b):
    m = a * b
    return m

def div(a,b):
    d = a / b
    return d

s = add(cc=4, aa=3, bb=2)
print("2,3 add is: ", s)

#
# r = sub(a,b)
# print("Sub value is: ", r)
#
# r = mul(a,b)
# print("Mul value is: ", r)
#
# r = div(a,b)
# print("Div value is: ", r)