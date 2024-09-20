from abc import ABC, abstractmethod
import numpy as np

class GenericMAS:

    def __init__(self, env, num_agents, seed, trace=False):
        self.environment = env
        self.trace = trace
        self.environment.mas = self
        self.agent_list = []
        self.initialize_agents(num_agents, seed)
        self.delay = 0.1  # Delay in seconds between turns

    def run_simulation(self, num_turns):
        for _ in range(num_turns):
            self.run_turn()

    @abstractmethod
    def initialize_agents(self, num_agents, seed):
        pass

    @abstractmethod
    def run_turn(self):
        pass
