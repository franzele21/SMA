"""
TODO:
    - index x/y sur les agents
"""
class Environnement():
    def __init__(self, largeur, hauteur, liste_agent, tor=False) -> None:
        self.largeur = largeur
        self.hauteur = hauteur
        self.agents = liste_agent
        self.agents_x = [[] for x in range(self.largeur)]
        self.agents_y = [[] for x in range(self.hauteur)]
        self.actualise_position()
        self.tor = tor
    
    def actualise_position(self):
        for agent_ in self.agents:
            self.agents_x[agent_.pos_x].append(agent_)
            self.agents_y[agent_.pos_y].append(agent_)

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
    
    def voisinage(self, pos_x, pos_y, envergure):
        if self.tor:
            pass
        else:
            lower_x = pos_x-envergure if pos_x-envergure >= 0 else 0
            upper_x = pos_x+envergure if pos_x+envergure < self.largeur else self.largeur-1
            lower_y = pos_y-envergure if pos_y-envergure >= 0 else 0
            upper_y = pos_y+envergure if pos_y+envergure < self.hauteur else self.hauteur-1
        voisins_x = [y for x in self.agents_x[lower_x:upper_x+1] for y in x]
        voisins_y = [y for x in self.agents_y[lower_y:upper_y+1] for y in x]

        voisins = list(set(voisins_x) & set(voisins_y))
        voisins = [x for x in voisins if pos_x!=x.pos_x or pos_y!=x.pos_y]

        return voisins
