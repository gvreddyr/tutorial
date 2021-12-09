import json

f = open("book.json")
d = json.load(f)
f.close()

authors = []
for k,v in d.items():
    for e in v:
        for k1,v1 in e.items():
            if k1 == 'author':
                authors.append(v1)

print("Authors:", authors)
