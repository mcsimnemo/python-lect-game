import random
from array import *
from agents import *
from nature import *

class GameWorld(object):
    def __init__(self, x, y):
        self.size_x = x
        self.size_y = y
        self.game_objects = []
        self.game_terrain = [[0] * x for i in range(y)] # matrix x * y filled with 0
        self.game_time = 0

    def add_object(self, object):
        print("Add object to the World")
        self.game_objects.append(object)


    def add_nature(self, object):
        x = object.position_x
        y = object.position_y
        if self.game_terrain[y][x] == 0:
            self.add_object(object)
            if object.type == "Derevo":
                self.game_terrain[y][x] = 0x2663
            return True
        else:
            return False





    def delete_object(self, object):
        print("Delete object to the World")
        self.game_objects.remove(object)

    def update_time(self):
        for obj in self.game_objects:
            if obj.__class__ == Nature:
                obj.add_resource()
                print("Nature %s with resource %d" %
                      (obj.type, obj.resource))

            if obj.__class__ == Agent:
                obj.heal(1)
                print("Agent in pos %d %d with health %d" %
                      (obj.position_x, obj.position_y, obj.health))
            # print(obj)
        self.game_time += 1

    def print_world(self):
        for y in range(self.size_y):
            str_out = ''
            for x in range(self.size_x):
                if self.game_terrain[y][x] == 0:
                    char_out = chr(0x2591)
                else:
                    char_out = chr(self.game_terrain[y][x])
                str_out += char_out
            print(str_out)


