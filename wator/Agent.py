"""
TODO:
    - prng dans le le choix de direction
    - décompte gestation/faim
    - généralisation de poissons/requin into creature_marine
    - mettre une variable eaten pour les poissons pour dire quil a été mangé par un requin pour que pas deux requins mange le meme poisson
"""


from core.GenericAgent import GenericAgent
import numpy as np

class Poisson(GenericAgent):
    def __init__(self, pos_x, pos_y, gestation=1, faim=0, color="cyan", trace=False):
        super().__init__(pos_x, pos_y, color, trace)
        self.gestation_max = gestation
        self.gestation_act = gestation
        self.deplace = False
    
    def decide(self, environement):
        # Se déplacent aléatoirement
        self.deplace = False
        self.gestation_act -= 1
        tout_agent = [agent for liste in environement.mas.agent_list for agent in liste]
        agent_proche = [(agent.pos_x, agent.pos_y) for agent in tout_agent if 
                            agent.pos_x in [self.pos_x-1, self.pos_x, self.pos_x+1] 
                            and agent.pos_y in [self.pos_y-1, self.pos_y, self.pos_y+1]]

        deplacement_possible = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
        deplacement_possible = [x for x in deplacement_possible if x not in agent_proche]

        if len(deplacement_possible)>0:
            self.deplace = True
            nouveau_deplacement = deplacement_possible[np.random.randint(len(deplacement_possible)-1)]

        # Si leurs période de gestation atteinte + peut se déplacer, 
        # alors bébé nait sur l'ancienne position
        nouveau_ne = self.mets_bas()

        est_mort = self.meurt()

        self.pos_x, self.pos_y = nouveau_deplacement
        return {"mets_bas": nouveau_ne, "meurt": est_mort, "poisson_gobe": None}

    def mets_bas(self):
        if self.deplace and self.gestation_act == 0:
            return Poisson(pos_x=self.pos_x,
                           pos_y=self.pos_y,
                           gestation=self.gestation_max,
                           trace=self.trace)
        elif self.gestation_act <= 0:
            self.gestation_act = self.gestation_max
        return False

    def meurt(self):
        return False
    
class Requin(GenericAgent):
    def __init__(self, pos_x, pos_y, gestation=3, faim=3, color="red", trace=False):
        super().__init__(pos_x, pos_y, color, trace)
        self.gestation_max = gestation
        self.gestation_act = gestation
        
        self.deplace = False

        self.faim_max = faim                # Nombre d'itérations sans manger possible
        self.faim_act = faim                # Nombre d'itérations restantes sans manger

    def decide(self, environnement):
        # Si compteur de faim tombe à 0 -> meurt
        if self.meurt:
            return {"mets_bas": False, "meurt": True, "poisson_gobe": None}       # he just like me fr
        
        # Se déplacent vers un poisson proche si il en voit un,
        # sinon déplacement aléatoire
        self.deplace = False
        self.gestation_act -= 1
        poisson_mange = None

        poissons = environnement.mas.agent_list[0]
        poissons_proche = [agent for agent in poissons if 
                            agent.pos_x in [self.pos_x-1, self.pos_x, self.pos_x+1] 
                            and agent.pos_y in [self.pos_y-1, self.pos_y, self.pos_y+1]]
        
        if len(poissons_proche) > 0:
            self.deplace = True
            self.faim_act = self.faim_max
            poisson_mange = np.random.choice(poissons_proche)
            nouveau_deplacement = (poisson_mange.pos_x, poisson_mange.pos_y)
        else:
            self.faim_act -= 1
            requins = environnement.mas.agent_list[1]
            requins_proche = [(agent.pos_x, agent.pos_y) for agent in requins if 
                            agent.pos_x in [self.pos_x-1, self.pos_x, self.pos_x+1] 
                            and agent.pos_y in [self.pos_y-1, self.pos_y, self.pos_y+1]]
            deplacement_possible = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
            deplacement_possible = [x for x in deplacement_possible if x not in requins_proche]
            if len(deplacement_possible) > 0:
                self.deplace = True
                nouveau_deplacement = deplacement_possible[np.random.randint(len(deplacement_possible)-1)]

        # Si leurs période de gestation atteinte + peut se déplacer,
        # alors bébé nait sur l'ancienne position
        nouveau_ne = self.mets_bas()
        
        self.pos_x, self.pos_y = nouveau_deplacement
        return {"mets_bas": nouveau_ne, "meurt": self.meurt, "poisson_gobe": poisson_mange} 

    def mets_bas(self):
        if self.deplace and self.gestation_act == 0:
            return Requin(pos_x=self.pos_x,
                           pos_y=self.pos_y,
                           gestation=self.gestation_max,
                           faim=self.faim_max,
                           trace=self.trace)
        elif self.gestation_act <= 0:
            self.gestation_act = self.gestation_max
        return False

    def meurt(self):
        return self.faim_act <= 0
