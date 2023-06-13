def param_check_decorator(func):
    def inner(*kargs):
        if len(kargs) < 2:
            return None
        for arg in kargs:
            if not isinstance(arg, int):
                return None
        return func(*kargs)
    return inner

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
