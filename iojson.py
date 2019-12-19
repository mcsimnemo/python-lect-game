import json

with open("data.json", "r") as read_file:
    data = json.load(read_file)
    

# print(data)

for key in data.keys():
    print(data[key])

size_x = data['size_x']
size_y = data['size_y']
level_name = data['level_name']

for tree in data['trees']:
    print(tree['x'])
    print(tree['y'])
    print(tree['resource'])
    print(tree['Type'])    
