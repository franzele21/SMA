"""
TODO:
    - faire en sorte que c'est l'agent qui regarde dans l'environnement
"""


import numpy as np

class Agent():
    def __init__(self, pos_x, pos_y, 
                 dir_x=np.random.choice([-1, 0, 1]), 
                 dir_y=np.random.choice([-1, 0, 1]), 
                 couleur=None
                 ) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_proch_x = pos_x
        self.pos_proch_y = pos_x
        self.dir_x = dir_x
        self.dir_y = dir_y
        if isinstance(couleur, type(None)):
            color = [str(x) for x in range(10)] + ["a", "b", "c", "d", "e", "f"]
            self.couleur = "#"+"".join(np.random.choice(color, size=3))
        else:
            self.couleur = couleur
    
    def __repr__(self):
        return f" |{self.pos_x} {self.pos_y}| "
    
    def predit(self):
        self.pos_proch_x += self.dir_x
        self.pos_proch_y += self.dir_y

    def update(self):
        self.pos_x = self.pos_proch_x
        self.pos_y = self.pos_proch_y

    def decide(self, env):
        agent_liste = env.voisinage(self.pos_x, self.pos_y, 1)
        if agent_liste:
            for agent in agent_liste:
                if agent != self:
                    if agent.pos_x == self.pos_x+self.dir_x \
                            and agent.pos_y == self.pos_y+self.dir_y \
                            and agent.pos_y != self.pos_y \
                            or agent.pos_x != self.pos_x:
                        if agent.dir_x == 0 and agent.dir_y == 0:
                            agent.dir_x = self.dir_x
                            agent.dir_y = self.dir_y
                            self.dir_x = -self.dir_x
                            self.dir_y = -self.dir_y
                        else:
                            self.dir_x, agent.dir_x = agent.dir_x, self.dir_x
                            self.dir_y, agent.dir_y = agent.dir_y, self.dir_y
        