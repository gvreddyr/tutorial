debug = False
t = 100
def sample():
    global t
    t = 101
    if debug:
        print(t)

def sample2():
    global t
    t = 102
    if debug:
        print(t)


sample() #global value changed from 100->101
sample2() #local variable value 12 and it doesn't affect global one
if debug:
    print(t)
