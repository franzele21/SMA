import numpy as np
import time
import sys
sys.path.insert(0, '..')
from hunter.Agent import Mur, Hunter, Avatar
from core.GenericMAS import GenericMAS

class MAS(GenericMAS):
    def __init__(self, env, seed, delay, trace=False):
        super().__init__(env, None, seed, delay, trace)

    def run_turn(self):
        self.environment.update_display()

        self.avatar.decide(self.environment)        
        
        time.sleep(self.delay)  # Add delay after each turn

    def pose_murs(self, murs, degradation):
        for pos_y in range(len(murs)):
            for pos_x in range(len(murs[0])):
                if murs[pos_y][pos_x] and self.prng.random() > degradation:
                    self.agent_list.append(Mur(pos_x, pos_y))

    def initialize_agents(self, num_agents, seed):
        positions = set()
        self.prng = np.random.default_rng(seed)
        self.avatar = Avatar(0, 0)
        self.agent_list.append(self.avatar)



        # for nb_agent in range(num_agents):
        #     added_agent = 0
        #     while added_agent < nb_agent:
        #         x = prng.integers(0, self.environment.width - 1)
        #         y = prng.integers(0, self.environment.height - 1)
        #         if (x, y) not in positions:
        #             positions.add((x, y))
        #             self.agent_list.append(agent_type(x, y, trace=self.trace))
        #             added_agent += 1
