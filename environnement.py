"""
TODO:
    - index x/y sur les agents
"""
class Environnement():
    def __init__(self, largeur, hauteur, liste_agent) -> None:
        self.largeur = largeur
        self.hauteur = hauteur
        self.agents = liste_agent

    def bordure(self, agent):
        if agent.pos_x+agent.dir_x < 0 or agent.pos_x+agent.dir_x > self.largeur-1:
            agent.dir_x = -agent.dir_x
        if agent.pos_y+agent.dir_y < 0 or agent.pos_y+agent.dir_y > self.hauteur-1:
            agent.dir_y = -agent.dir_y
        # on vérifie si il n'y a pas déjà un agent sur la case future

    def check_agent_a_pos(self, x, y):
        for agent in self.agents:
            if agent.pos_x == x and agent.pos_y == y:
                return agent
        return False