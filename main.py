"""
TODO:
    - faire la trace dans un fichier CSV
"""

import numpy as np
import mas
import environnement
import agent
import random

import json

import tkinter as tk
import time

def reset_canva(canva, height, width, box_size):
    canva.delete("all")
    dash_length = 1+box_size//2
    pixel_height = height*box_size
    for i in range(width):
        canva.create_line((i*box_size, 0), (i*box_size, pixel_height), fill="grey", dash=(dash_length))
    pixel_width = width*box_size
    for i in range(height):
        canva.create_line((0, i*box_size), (pixel_width, i*box_size), fill="grey", dash=(dash_length))

def set_agent_on_canva(canva, agent, box_size):
    canva.create_oval(agent.pos_x*box_size, agent.pos_y*box_size, agent.pos_x*box_size+box_size, agent.pos_y*box_size+box_size, fill=agent.couleur)

with open("config.json") as file:
    config = json.load(file)
config["seed"] = config["seed"] if config["seed"] != 0 else random.random()

rng = np.random.default_rng(config["seed"])

agent_list = mas.create_agent(rng, config["nb_particules"], config["width"], config["height"])

env = environnement.Environnement(config["width"],
                                  config["height"], 
                                  agent_list)
mas_ = mas.MAS(env)

window = tk.Tk()
win_height = config["box_size"]*config["height"]
win_width = config["box_size"]*config["width"]
window.geometry(f"{win_width}x{win_height}")

cv = tk.Canvas(window, width=win_width, height=win_height, bg="white")
cv.pack(expand=True)

if config["trace"]:
    traceur = {agent_.couleur: [[int(agent_.pos_x), int(agent_.pos_y)]] for agent_ in agent_list}

ticks = config["ticks"] if config["ticks"] > 0 else 100000000000000
for i in range(ticks):
    reset_canva(cv, config["height"], config["width"], config["box_size"])
    for agent_ in env.agents:
        if config["trace"]:
            traceur[agent_.couleur].append([int(agent_.pos_x), int(agent_.pos_y)])
        set_agent_on_canva(cv, agent_, config["box_size"])
    time.sleep(config["pause"])
    window.update()
    mas_.run()

print(traceur)
if config["trace"]:
    with open("trace.json", "w+", encoding='utf-8') as file:
        json.dump(traceur, file, ensure_ascii=False, indent=1)