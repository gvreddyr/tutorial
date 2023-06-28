x = 200

def print_x():
    global x
    x = 400
    print("X-F:", x)


print("X1: ",x)

x = 300
print("X2: ",x)

print_x()

print("X3: ",x)
