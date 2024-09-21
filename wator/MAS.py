"""
TDOD:
    - mettre tous les agents dans une seule liste (le système act ne fonctionne pas avec genericenvironemn)
"""

import numpy as np
import time
from wator.Agent import Poisson, Requin
from core.GenericMAS import GenericMAS

class MAS(GenericMAS):
    def __init__(self, env, nb_poissons, nb_requins, gest_pois, gest_requ, faim_requ, seed, trace=False):
        self.gest_pois = gest_pois
        self.gest_requ = gest_requ
        self.faim_requ = faim_requ
        super().__init__(env, [nb_poissons, nb_requins], seed, trace)

    def run_turn(self):
        dead_creature = [[], []]
        new_creature = [[], []]
        for i, creatures_liste in enumerate(self.agent_list):
            for agent in creatures_liste:
                effect = agent.decide(self.environment)
                if effect["mets_bas"]:
                    new_creature[i].append(effect["mets_bas"])
                if effect["meurt"]:
                    dead_creature[i].append(effect["meurt"])
                if effect["poisson_gobe"]:
                    dead_creature[0].append(effect["poisson_gobe"])
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

        self.agent_list = [[], []]
        for i, (nb_agent, agent_type, arg_type) in enumerate(zip(num_agents, [Poisson, Requin], params)):
            while len(self.agent_list[i]) < nb_agent:
                x = prng.integers(0, self.environment.width - 1)
                y = prng.integers(0, self.environment.height - 1)
                if (x, y) not in positions:
                    positions.add((x, y))
                    self.agent_list[i].append(agent_type(x, y, gestation=arg_type[0], faim=arg_type[1], trace=self.trace))
