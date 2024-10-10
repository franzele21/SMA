import sys
sys.path.insert(0, '..')
from core.GenericAgent import GenericAgent
import numpy as np
import random
import heapq


class Mur(GenericAgent):
    def __init__(self, pos_x, pos_y, color="black", trace=False):
        super().__init__(pos_x, pos_y, color, trace)

    def decide(self, environnement):
        pass

class Hunter(GenericAgent):
    def __init__(self, pos_x, pos_y, color="red", trace=False):
        super().__init__(pos_x, pos_y, color, trace)
        self.dir_x = 0
        self.dir_y = 0

    def manhattan(self, a, b):
        return sum(abs(val1-val2) for val1, val2 in zip(a,b))

    def get_neighbors(self, x, y, environnement):
        neighbors = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < environnement.width and 0 <= ny < environnement.height:
                neighbors.append((nx, ny))
        return neighbors

    def is_valid_move(self, x, y, environnement):
        for agent in environnement.mas.agent_list:
            if isinstance(agent, Mur) and agent.pos_x == x and agent.pos_y == y:
                return False
        return True

    def astar(self, start, goal, environnement):
        heap = [(0, start)]
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.manhattan(start, goal)}

        while heap:
            current = heapq.heappop(heap)[1] #file a priorité pour garder le meilleur chemin à portée de main

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

            for neighbor in self.get_neighbors(*current, environnement):
                if not self.is_valid_move(*neighbor, environnement):
                    continue

                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.manhattan(neighbor, goal)
                    heapq.heappush(heap, (f_score[neighbor], neighbor))

        return None

    def decide(self, environnement):
        cible = [agent for agent in environnement.mas.agent_list if isinstance(agent, Avatar)][0]
        start = (self.pos_x, self.pos_y)
        goal = (cible.pos_x, cible.pos_y)

        path = self.astar(start, goal, environnement)

        if path and len(path) > 1:
            next_pos = path[1]
            self.dir_x = next_pos[0] - self.pos_x
            self.dir_y = next_pos[1] - self.pos_y
        else:
            self.dir_x = 0
            self.dir_y = 0

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
        hunter_proche = [agent for agent in agent_proche if isinstance(agent, Hunter)]
        deplacement_possible = [[x, y] for x in range(-1, 2) for y in range(-1, 2)]
        deplacement_possible = [x for x in deplacement_possible if x not in mur_proche]
        for mur in mur_proche:
            if [self.pos_x+self.dir_x, self.pos_y+self.dir_y] == [mur.pos_x, mur.pos_y]:
                self.dir_y=0
                self.dir_x=0

        for avatar in hunter_proche:
            if ([self.pos_x, self.pos_y] == [avatar.pos_x, avatar.pos_y]):
                print("HUNTER WINS")
                sys.exit(0)
        
        self.pos_x += self.dir_x
        self.pos_y += self.dir_y