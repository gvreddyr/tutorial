import json

file_name = "../data/menu.json"
data = None
with open(file_name) as f:
    data = json.load(f)
    print(data['menu']['popup']['menuitem'][2]['onclick'])

file_name = "../data/menu_new.json"
with open(file_name, 'w') as f:
    json.dump(data, f)