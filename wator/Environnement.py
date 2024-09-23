import sys
sys.path.insert(0, '..')
from core.GenericEnvironment import GenericEnvironment

class Environment(GenericEnvironment):
    def __init__(self, width, height, cell_size, torus=False):
        super().__init__(width, height, cell_size, torus)
