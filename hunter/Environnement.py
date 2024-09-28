import sys
sys.path.insert(0, '..')
from core.GenericEnvironment import GenericEnvironment

class Environment(GenericEnvironment):
    def __init__(self, width, height, cell_size, torus=False):
        super().__init__(width, height, cell_size, torus)
        self.dir = None
        self.root.bind("<Left>", lambda event: self.change_direction("O"))
        self.root.bind("<Right>", lambda event: self.change_direction("E"))
        self.root.bind("<Down>", lambda event: self.change_direction("S"))
        self.root.bind("<Up>", lambda event: self.change_direction("N"))
    
    def change_direction(self, direction):
        self.dir = direction
        print("env", self.dir)