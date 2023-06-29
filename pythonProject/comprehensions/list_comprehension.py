l = [5,4,2,3,1,7,6,9,8,0]

#el = [i*3 for i in l if i % 2 != 0]

el = [i*3 if i % 2 != 0 else i*2 for i in l]

o = []
for i in l:
    if i % 2 != 0:
        o.append(i*3)
    else:
        o.append(i*2)

print(o)
print(el)