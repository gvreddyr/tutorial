l = [5,4,2,3,1,7,6,9,8,0]
l1 = [10,8,4,6,2,14,12,18,16,0]

d = dict(zip(l,l1))
print(d)

od = {2*i:2*j for i,j in d.items()}
print(od)