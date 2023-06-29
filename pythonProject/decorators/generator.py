def func1():
    for i in range(10):
        yield i
        print(f"I'm after yield {i}")



g = func1()

for i in g:
    print(f"I'm in func1 and value of i is {i}")
