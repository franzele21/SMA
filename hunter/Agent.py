import sys
sys.path.insert(0, '..')
from core.GenericAgent import GenericAgent
import numpy as np
import random
import heapq


class Mur(GenericAgent):
    def __init__(self, pos_x, pos_y, color="white", trace=False):
        super().__init__(pos_x, pos_y, color, trace)

    def decide(self, environnement):
        pass

class Hunter(GenericAgent):
    def __init__(self, pos_x, pos_y, color="red", trace=False):
        super().__init__(pos_x, pos_y, color, trace)
        self.dir_x = 0
        self.dir_y = 0
        self.potential_paths = []

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

    def astar(self, start, goal, environnement, max_paths=5, max_length=20):
        heap = [(0, start, [])]
        visited = set()
        paths_found = []

        while heap and len(paths_found) < max_paths:
            _, current, path = heapq.heappop(heap)

            if current == goal:
                paths_found.append(path + [current])
                continue

            if len(path) >= max_length:
                paths_found.append(path + [current])
                continue

            if current not in visited:
                visited.add(current)

                for neighbor in self.get_neighbors(*current, environnement):
                    if self.is_valid_move(*neighbor, environnement):
                        new_path = path + [current]
                        priority = len(new_path) + self.manhattan(neighbor, goal)
                        heapq.heappush(heap, (priority, neighbor, new_path))

        return paths_found

    def decide(self, environnement):
        cible = next(agent for agent in environnement.mas.agent_list if isinstance(agent, Avatar))
        start = (self.pos_x, self.pos_y)
        goal = (cible.pos_x, cible.pos_y)

        self.potential_paths = self.astar(start, goal, environnement)

        if self.potential_paths and len(self.potential_paths[0]) > 1:
            next_pos = self.potential_paths[0][1]
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

        self.pos_x += self.dir_x
        self.pos_y += self.dir_y