from ..core.GenericAgent import GenericAgent

class Poisson(GenericAgent):
    def __init__(self, pos_x, pos_y, color="cyan", trace=False):
        super().__init__(pos_x, pos_y, color, trace)
    
    def decide(self, environement):
        # Si possible, s'éloigne des requins
        pass

    def get_color(self):
        return self.color
    
class Requin(GenericAgent):
    def __init__(self, pos_x, pos_y, color="red", trace=False):
        super().__init__(pos_x, pos_y, color, trace)
    
    
