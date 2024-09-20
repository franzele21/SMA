import tkinter as tk
import random
import sys
sys.path.append("..")
from core.GenericEnvironment import GenericEnvironment 

class Environment(GenericEnvironment):
    def __init__(self, width, height, cell_size, torus=False):
        super().__init__(width, height, cell_size, torus)
