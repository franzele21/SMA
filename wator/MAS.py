import numpy as np
import time
from wator.Agent import Poisson, Requin
from ..core.GenericMAS import GenericMAS

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
                if prng.random() < 0.5:
                    self.agent_list.append(Poisson(x, y, "cyan", self.trace))
                else:
                    self.agent_list.append(Requin(x, y, "red", self.trace))