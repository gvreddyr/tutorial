import json
s = '''
{"menu": {  
  "id": "file",  
  "value": "File",  
  "popup": {  
    "menuitem": [  
      {"value": "New", "onclick": "CreateDoc()"},  
      {"value": "Open", "onclick": "OpenDoc()"},  
      {"value": "Save", "onclick": "SaveDoc()"}  
    ]  
  }  
}}'''

data = json.loads(s)
print(data['menu']['popup']['menuitem'][2]['onclick'])