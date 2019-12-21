from world import *
from nature import *
from agents import *
import json

def CreateAndLoadGame(file_name):
    with open(file_name, "r") as read_file:
        data = json.load(read_file)
    size_x = data['size_x']
    size_y = data['size_y']
    level_name = data['level_name'] 
    game_world = GameWorld(size_x, size_y)
        
    for data_tree in data['trees']:
        tree_x = data_tree['x']
        tree_y = data_tree['y']
        tree_res = data_tree['resource']
        tree_type = data_tree['Type']
#        tree = Nature(tree_type, tree_x, tree_y)
#        tree.resource = tree_res
        tree = Nature(tree_type, tree_x, tree_y, tree_res)
        game_world.add_nature(tree)
    
    return game_world


if __name__ == "__main__":
    my_game_world = CreateAndLoadGame("data.json")

    hero = Agent()
    my_game_world.add_object(hero)

    my_game_world.update_time()
    my_game_world.print_world()
