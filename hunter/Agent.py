import sys
sys.path.insert(0, '..')
from core.GenericAgent import GenericAgent

class Mur(GenericAgent):
    def __init__(self, pos_x, pos_y, color="black", trace=False):
        super().__init__(pos_x, pos_y, color, trace)

    def decide(self, environnement):
        pass

class Hunter(GenericAgent):
    def __init__(self, pos_x, pos_y, color="black", trace=False):
        super().__init__(pos_x, pos_y, color, trace)

    def decide(self, environnement):
        pass

class Avatar(GenericAgent):
    def __init__(self, pos_x, pos_y, color="green", trace=False):
        super().__init__(pos_x, pos_y, color, trace)
        self.dir_x = 0
        self.dir_y = 0

    def decide(self, environnement):
        new_dir = environnement.dir
        print("avatar", new_dir)
        match new_dir:
            case "O":
                self.dir_x = -1
                self.dir_y = 0
            case "E":
                self.dir_x = 1
                self.dir_y = 0
            case "S":
                self.dir_x = 0
                self.dir_y = 1
            case "N":
                self.dir_x = 0
                self.dir_y = -1
        self.pos_x += self.dir_x
        self.pos_y += self.dir_y