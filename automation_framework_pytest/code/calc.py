def param_check_decorator(func):
    def inner(*kargs):
        if len(kargs) < 2:
            return None
        for arg in kargs:
            if not isinstance(arg, int):
                return None
        res = func(*kargs)
        print("Result: %d"%res)
        return res
    return inner

'''
add(2,3, 4, 5, 6, 7, 8) --> invoking this functions

first it executes the param_check_decorator
then it actually call the add/sub/mul/div
'''


@param_check_decorator
def add(*kargs):
    r = 0
    for elem in kargs:
        r += elem
    return r

@param_check_decorator
def sub(*kargs):
    r = kargs[0]
    for elem in kargs[1:]:
        r -= elem
    return r


@param_check_decorator
def mul(*kargs):
    r = 1
    for elem in kargs:
        r *= elem
    return r


@param_check_decorator
def div(*kargs):
    r = kargs[0]
    for elem in kargs[1:]:
        r //= elem
    return r

