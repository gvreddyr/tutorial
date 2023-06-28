l = 100
x = 200
t = 4
name = "Rachamallu"

d = {'name': 'Govardhan',
     'profession': 'training',
     'duration': 2}

print("l value is: %d, x value is: %d"%(l,x))

print(f"l value is: {l}, x value is: {x}")

print(f"d value is: {d}")

print("My name is: %s, and I do training for %d hours"%(name, t))

print("My name is: {name}, and I do {profession} for {duration} hours".format(**d))
print("My name is: {}, and I do {} for {} hours".format(d['name'], d['profession'], d['duration']))
print("My name is: {}, and I do {} for {} hours".format(*d.values()))

print("l is {}, x is {}, t is {}".format(l,x,t))

print("l is {2}, x is {1}, t is {0}".format(t,x,l))



