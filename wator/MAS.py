"""
TDOD:
    - mettre tous les agents dans une seule liste (le système act ne fonctionne pas avec genericenvironemn)
"""

import numpy as np
import time
from wator.Agent import Poisson, Requin
from core.GenericMAS import GenericMAS

class MAS(GenericMAS):
    def __init__(self, env, nb_poissons, nb_requins, gest_pois, gest_requ, faim_requ, seed, delay, trace=False):
        self.gest_pois = gest_pois
        self.gest_requ = gest_requ
        self.faim_requ = faim_requ
        super().__init__(env, [nb_poissons, nb_requins], seed, delay, trace)

    def run_turn(self):
        dead_creature = []
        new_creature = []
        for agent in self.agent_list:
            print(agent.pos_x, agent.pos_y)
            effect = agent.decide(self.environment)
            if effect["mets_bas"]:
                new_creature.append(effect["mets_bas"])
            if effect["meurt"]:
                dead_creature.append(agent)
            if effect["poisson_gobe"]:
                dead_creature.append(effect["poisson_gobe"])

        for creature in dead_creature:
            index_ = self.agent_list.index([agent for agent in self.agent_list 
                      if agent.pos_x == creature.pos_x
                      and agent.pos_y == creature.pos_y
                      and agent.mort
                      and isinstance(agent, type(creature))][0])
            del self.agent_list[index_]
        for creature in new_creature:
            self.agent_list.append(creature)
        self.environment.update_display()
        time.sleep(self.delay)  # Add delay after each turn
        # ^^^^?????????

    def initialize_agents(self, num_agents, seed):
        positions = set()
        prng = np.random.default_rng(seed)
        params = [
            [self.gest_pois, 0],
            [self.gest_requ, self.faim_requ]
        ]

        for nb_agent, agent_type, arg_type in zip(num_agents, [Poisson, Requin], params):
            added_agent = 0
            while added_agent < nb_agent:
                x = prng.integers(0, self.environment.width - 1)
                y = prng.integers(0, self.environment.height - 1)
                if (x, y) not in positions:
                    print((x, y))
                    positions.add((x, y))
                    self.agent_list.append(agent_type(x, y, gestation=arg_type[0], faim=arg_type[1], trace=self.trace))
                    added_agent += 1
        print(self.agent_list)
