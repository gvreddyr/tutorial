with open("../data/example2.txt") as f:
    data = f.readlines()
    for line in data:
        print(line)

with open("../data/example3.txt", 'w') as f:
    f.write("Hi I'm writing it something more new\n")
    f.writelines(["1111\n", "2222\n", "33333\n"])

