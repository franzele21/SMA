"""
TODO:
    - laisser l'agent faire en sorte de s'appeller etc
"""
import numpy as np
from agent import Agent
from environnement import Environnement

def create_agent(rng, nb_agent, largeur_max, hauteur_max):
    liste_agent = []
    color = [str(x) for x in range(10)] + ["a", "b", "c", "d", "e", "f"]
    for i in range(nb_agent):
        liste_agent.append(Agent(rng.integers(largeur_max-1), 
                                 rng.integers(hauteur_max-1),
                                 rng.choice([-1, 0, 1]),
                                 rng.choice([-1, 0, 1]),
                                 "#"+"".join(rng.choice(color, size=3))))
    return liste_agent

class MAS():
    def __init__(self, 
                 env: Environnement
                 ) -> None:
        self.env = env

    def run(self):
        for agent1 in self.env.agents:
            self.env.bordure(agent1)
            agent1.decide(self.env)
            agent1.predit()
            print(agent1.couleur, agent1, agent1.pos_proch_x, agent1.pos_proch_y)
        for agent in self.env.agents:
            agent.update()