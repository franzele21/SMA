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
    def __init__(self, pos_x, pos_y, color="black", trace=False):
        super().__init__(pos_x, pos_y, color, trace)

    def decide(self, environnement):
        pass