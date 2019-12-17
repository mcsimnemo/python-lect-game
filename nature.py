
class Nature(object):
    def __init__(self, nature_type, x, y):
        self.type = nature_type
        self.position_x = x
        self.position_y = y
        self.resource = 1000  ## in futute make it randomef

    def get_resource(self):
        self.resource -= 10

    def add_resource(self):
        self.resource += 1
