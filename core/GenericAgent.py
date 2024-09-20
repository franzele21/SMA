from abc import ABC, abstractmethod

class GenericAgent(ABC):
    def __init__(self, pos_x, pos_y, color="blue", trace=False):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.trace = trace
        self.color = color

    @abstractmethod
    def decide(self, environement):
        pass
