import json
s = """{
   "book": [

      {
         "id":"01",
         "language": "Java",
         "edition": "third",
         "author": "Herbert Schildt"
      },

      {
         "id":"07",
         "language": "C++",
         "edition": "second",
         "author": "E.Balagurusamy"
      }
   ]
}"""

print(type(s))
d = json.loads(s)
print(type(d))
d["price"] = 1000
s = json.dumps(d)
print(type(s))
print(s)

f = open('newbook.json', 'w')
o = json.dump(d, f, indent=4)
f.close()
