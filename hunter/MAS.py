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
        if not self.environment.game_over:
            self.avatar.decide(self.environment)        
            self.hunter.decide(self.environment)
            
            # Check for game over condition
            if self.hunter.pos_x == self.avatar.pos_x and self.hunter.pos_y == self.avatar.pos_y:
                self.environment.game_over = True
                print("Game Over! Hunter caught the Avatar.")

        self.environment.update_display()
        time.sleep(self.delay)  # Add delay after each turn

    def pose_murs(self, murs, degradation):
        for pos_y in range(len(murs)):
            for pos_x in range(len(murs[0])):
                if murs[pos_y][pos_x] and self.prng.random() > degradation:
                    self.agent_list.append(Mur(pos_x, pos_y))
        self.actualise_position()

    def initialize_agents(self, num_agents, seed):
        self.prng = np.random.default_rng(seed)
        self.avatar = Avatar(0, 0)
        self.hunter = Hunter(self.environment.width-1, self.environment.height-1)
        self.agent_list.append(self.avatar)
        self.agent_list.append(self.hunter)
