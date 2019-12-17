
class Agent(object):
    def __init__(self):
        self.name = "Agent"
        self.position_x = -1
        self.position_y = -1
        self.health = 100

    def move_to(self, x, y):
        self.position_x = x
        self.position_y = y
        self.health -= 1

    def heal(self, health):
        self.health += health

    def attack(self):
        force = self.health * 0.25
        self.health -= self.health * 0.1
        return force

    def damage(self, force):
        self.health -= force
        return self.health


class Barbarian(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = "Barbarian"

    def heal(self, health):
        self.health += health / 2


class Skiph(Barbarian):
    def __init__(self):
        Agent.__init__(self)
        self.name = "Skiph"
        self.health = 80

    def attack(self):
        force = self.health * 0.20
        self.health -= self.health * 0.05
        return force

    def damage(self, force):
        self.health -= force * 0.95
        return self.health

    def move_to(self, x, y):
        Agent.move_to(self, x, y)
        self.health -= 0.1

    def heal(self, health):
        self.health += health / 1.5


class Elephant(Barbarian):
    def __init__(self):
        Agent.__init__(self)
        self.name = "Elephant"
        self.health = 200

    def attack(self):
        force = self.health * 0.80
        self.health -= self.health * 0.05

    def damage(self, force):
        self.health -= force * 0.85

    def move_to(self, x, y):
        Agent.move_to(self, x, y)
        self.health -= 5
