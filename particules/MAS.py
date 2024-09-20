import numpy as np
import time
from Agent import Agent
import sys
sys.path.append("..")
from core.GenericMAS import GenericMAS 

class MAS(GenericMAS):

    def __init__(self, env, num_agents, seed, trace=False):
        super().__init__(env, num_agents, seed, trace)

    def run_turn(self):
        for agent in self.agent_list:
            agent.decide(self.environment)
        self.environment.update_display()
        time.sleep(self.delay)  # Add delay after each turn

    def initialize_agents(self, num_agents, seed):
        positions = set()
        prng = np.random.default_rng(seed)
        while len(self.agent_list) < num_agents:
            x = prng.integers(0, self.environment.width - 1)
            y = prng.integers(0, self.environment.height - 1)
            if (x, y) not in positions:
                positions.add((x, y))
                color = prng.choice(["blue", "brown", "grey", "red", "yellow", "cyan", "green", "pink", "purple", "black", "orange"])
                self.agent_list.append(Agent(x, y, 
                                             prng.choice([-1, 0, 1]),
                                             prng.choice([-1, 0, 1]),
                                             color, 
                                             self.trace))
