"""
TODO:
    - faire en sorte que c'est l'agent qui regarde dans l'environnement
"""


import numpy as np

class Agent():
    def __init__(self, pos_x, pos_y, 
                 dir_x=np.random.choice([-1, 0, 1]), 
                 dir_y=np.random.choice([-1, 0, 1]), 
                 couleur=list(np.random.choice(range(256), size=3))
                 ) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.couleur = couleur
        self.trajectoire_changee = False
    
    def __repr__(self):
        return f" |{self.pos_x} {self.pos_y}| "

    def update(self):
        self.pos_x += self.dir_x
        self.pos_y += self.dir_y

    def decide(self, agent):
        if agent != self:
            if agent.dir_x == 0 and agent.dir_y == 0:
                agent.dir_x = self.dir_x
                agent.dir_y = self.dir_y
                self.dir_x = -self.dir_x
                self.dir_y = -self.dir_y
            else:
                self.dir_x, agent.dir_x = agent.dir_x, self.dir_x
                self.dir_y, agent.dir_y = agent.dir_y, self.dir_y
        