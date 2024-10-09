import sys
sys.path.insert(0, '..')
from core.GenericAgent import GenericAgent
import numpy as np
import random


class Mur(GenericAgent):
    def __init__(self, pos_x, pos_y, color="black", trace=False):
        super().__init__(pos_x, pos_y, color, trace)

    def decide(self, environnement):
        pass

class Hunter(GenericAgent):
    def __init__(self, pos_x, pos_y, color="red", trace=False):
        super().__init__(pos_x, pos_y, color, trace)

    def decide(self, environnement):
        agent_proche = environnement.mas.voisinage(self.pos_x, self.pos_y, 1)
        random_dir_x = random.choice([-1, 0, 1])
        random_dir_y = random.choice([-1, 0, 1])

        self.dir_x = random_dir_x
        self.dir_y = random_dir_y
        
        if not environnement.torus:
            if self.pos_x +self.dir_x < 0 or self.pos_x+self.dir_x > environnement.width-1:
                self.dir_x = 0
            if self.pos_y +self.dir_y < 0 or self.pos_y+self.dir_y > environnement.height-1:
                self.dir_y = 0

        mur_proche = [agent for agent in agent_proche if isinstance(agent, Mur)]
        avatar_proche = [agent for agent in agent_proche if isinstance(agent, Avatar)]
        deplacement_possible = [[x, y] for x in range(-1, 2) for y in range(-1, 2)]
        deplacement_possible = [x for x in deplacement_possible if x not in mur_proche]
        for mur in mur_proche:
            if [self.pos_x+self.dir_x, self.pos_y+self.dir_y] == [mur.pos_x, mur.pos_y]:
                self.dir_y=0
                self.dir_x=0
        
        for avatar in avatar_proche:
            [self.pos_x+self.dir_x, self.pos_y+self.dir_y] == [avatar.pos_x, avatar.pos_y]
            sys.exit(0)
        
        self.pos_x += self.dir_x
        self.pos_y += self.dir_y

class Avatar(GenericAgent):
    def __init__(self, pos_x, pos_y, color="green", trace=False):
        super().__init__(pos_x, pos_y, color, trace)
        self.dir_x = 0
        self.dir_y = 0

    def decide(self, environnement):
        new_dir = environnement.dir
        agent_proche = environnement.mas.voisinage(self.pos_x, self.pos_y, 1)
        # print("voisin",agent_proche)
        # print("avatar", new_dir)
        match new_dir:
            case "O":
                self.dir_x = -1
                self.dir_y = 0
            case "E":
                self.dir_x = 1
                self.dir_y = 0
            case "S":
                self.dir_x = 0
                self.dir_y = 1
            case "N":
                self.dir_x = 0
                self.dir_y = -1
        
        if not environnement.torus:
            if self.pos_x +self.dir_x < 0 or self.pos_x+self.dir_x > environnement.width-1:
                self.dir_x = 0
            if self.pos_y +self.dir_y < 0 or self.pos_y+self.dir_y > environnement.height-1:
                self.dir_y = 0

        mur_proche = [agent for agent in agent_proche if isinstance(agent, Mur)]
        deplacement_possible = [[x, y] for x in range(-1, 2) for y in range(-1, 2)]
        deplacement_possible = [x for x in deplacement_possible if x not in mur_proche]
        for mur in mur_proche:
            if [self.pos_x+self.dir_x, self.pos_y+self.dir_y] == [mur.pos_x, mur.pos_y]:

                self.dir_y=0
                self.dir_x=0
        
        self.pos_x += self.dir_x
        self.pos_y += self.dir_y