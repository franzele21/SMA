from abc import ABC, abstractmethod
import numpy as np

class GenericAgent(ABC):

    def __init__(self, pos_x, pos_y, color="blue", trace=False):
        prng = np.random.default_rng(12345)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.trace = trace
        self.dir_x = prng.choice([-1, 0, 1])
        self.dir_y = prng.choice([-1, 0, 1])
        self.color = color

    @abstractmethod
    def decide(self, environement):
        pass
