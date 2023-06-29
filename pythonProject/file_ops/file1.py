'''
text
    alphabets, numbers, symbols
        csv - comma separated values
        json - java script object notation
        xml - markup language
        html
        txt
bin
    image, doc/xl/ppt, audio/video

operations:
    read
    write
    `   update
        insert
'''


file_path = "../data/example.txt"



f = open(file_path)
print(type(f))
data = f.read()
print(type(data))
print(data)
f.close()

f = open(file_path)

x = 10
#x = x // 0
data = f.readlines()
print(data)
print("read lines##########")
for line in data:
    print(line)

f.close()


with open(file_path) as f:
    x = 10
    x = x // 0
    data = f.readlines()
    print(data)
    print("read lines##########")
    for line in data:
        print(line)

