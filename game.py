from world import *
from nature import *
from agents import *

if __name__ == "__main__":
    my_game_world = GameWorld(15, 10)

    tree = Nature("Derevo", 3, 4)
    my_game_world.add_nature(tree)

    tree = Nature("Derevo", 7, 2)
    my_game_world.add_nature(tree)

    hero = Agent()
    my_game_world.add_object(hero)

    my_game_world.update_time()
    my_game_world.print_world()
