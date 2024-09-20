from core.GenericAgent import GenericAgent

class Agent(GenericAgent):
    def __init__(self, pos_x, pos_y, dir_x, dir_y, color="gray", trace=False):
        super().__init__(pos_x, pos_y, color, trace)
        self.dir_x = dir_x
        self.dir_y = dir_y

    def decide(self, environment):
        new_x = (self.pos_x + self.dir_x) % environment.width if environment.torus else self.pos_x + self.dir_x
        new_y = (self.pos_y + self.dir_y) % environment.height if environment.torus else self.pos_y + self.dir_y

        # Check for collisions with boundaries if not torus
        if not environment.torus:
            if new_x < 0 or new_x >= environment.width:
                self.dir_x *= -1
                new_x = self.pos_x
            if new_y < 0 or new_y >= environment.height:
                self.dir_y *= -1
                new_y = self.pos_y

        # Check for collisions with other agents
        for agent in environment.mas.agent_list:
            if agent != self and agent.pos_x == new_x and agent.pos_y == new_y:
                if self.trace:
                    print(f"Agent {self.color}; Agent {agent.color}")
                self.dir_x, agent.dir_x = agent.dir_x, self.dir_x
                self.dir_y, agent.dir_y = agent.dir_y, self.dir_y
                new_x, new_y = self.pos_x, self.pos_y
                # self.color = "red"
                # agent.color = "red"
                break

        self.pos_x, self.pos_y = new_x, new_y
