from abc import ABC, abstractmethod

class GenericMAS:
    def __init__(self, env, num_agents, seed, delay, trace=False):
        self.environment = env
        self.trace = trace
        self.environment.mas = self
        self.agent_list = []
        self.initialize_agents(num_agents, seed)
        self.delay = delay  # Delay in seconds between turns

        self.agents_x = [[] for x in range(self.environment.width)]
        self.agents_y = [[] for x in range(self.environment.height)]
        self.actualise_position()

    def run_simulation(self, num_turns):
        for _ in range(num_turns):
            self.run_turn()

    @abstractmethod
    def initialize_agents(self, num_agents, seed):
        pass

    @abstractmethod
    def run_turn(self):
        pass

    def voisinage(self, pos_x, pos_y, envergure):
        if self.environment.torus:
            pass
        else:
            lower_x = pos_x-envergure if pos_x-envergure >= 0 else 0
            upper_x = pos_x+envergure if pos_x+envergure < self.environment.width else self.environment.width-1
            lower_y = pos_y-envergure if pos_y-envergure >= 0 else 0
            upper_y = pos_y+envergure if pos_y+envergure < self.environment.height else self.environment.height-1
        voisins_x = [y for x in self.agents_x[lower_x:upper_x+1] for y in x]
        voisins_y = [y for x in self.agents_y[lower_y:upper_y+1] for y in x]

        voisins = list(set(voisins_x) & set(voisins_y))
        voisins = [x for x in voisins if pos_x!=x.pos_x or pos_y!=x.pos_y]

        return voisins

    def actualise_position(self):
        for agent_ in self.agent_list:
            self.agents_x[agent_.pos_x].append(agent_)
            self.agents_y[agent_.pos_y].append(agent_)
