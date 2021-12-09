f = open("1.txt", 'r')
#o = f.read()
#o = f.readlines()
for i in f:
    if "line 8" in i:
        print(i)
f.close()
