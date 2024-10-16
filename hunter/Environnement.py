import sys
sys.path.insert(0, '..')
from core.GenericEnvironment import GenericEnvironment
from hunter.Agent import Hunter, Avatar, Mur
import tkinter as tk
import colorsys

class Environment(GenericEnvironment):
    def __init__(self, width, height, cell_size, torus=False):
        super().__init__(width, height, cell_size, torus)
        self.dir = None
        self.root.bind("<Left>", lambda event: self.change_direction("O"))
        self.root.bind("<Right>", lambda event: self.change_direction("E"))
        self.root.bind("<Down>", lambda event: self.change_direction("S"))
        self.root.bind("<Up>", lambda event: self.change_direction("N"))

    def change_direction(self, direction):
        self.dir = direction
        print("env", self.dir)

    def draw_agents(self):
        self.canvas.delete("all")
        
        # Find Hunter and Avatar
        hunter = next((agent for agent in self.mas.agent_list if isinstance(agent, Hunter)), None)
        avatar = next((agent for agent in self.mas.agent_list if isinstance(agent, Avatar)), None)
        
        if hunter and avatar and hasattr(hunter, 'potential_paths'):
            # Draw Hunter's potential paths
            max_distance = self.width + self.height  # Maximum possible distance
            for path in hunter.potential_paths:
                for i, pos in enumerate(path):
                    x, y = pos
                    distance = abs(x - avatar.pos_x) + abs(y - avatar.pos_y)
                    intensity = 1 - (distance / max_distance)
                    color = self.get_gradient_color(intensity)
                    
                    self.canvas.create_rectangle(
                        x * self.cell_size, y * self.cell_size,
                        (x + 10) * self.cell_size, (y + 10) * self.cell_size,
                        fill=color, outline="", tags="path"
                    )

        for agent in self.mas.agent_list:
            x = agent.pos_x * self.cell_size
            y = agent.pos_y * self.cell_size
            if isinstance(agent, (Hunter, Avatar)):
                # Draw Hunter and Avatar as ovals
                self.canvas.create_oval(
                    x + 2, y + 2, 
                    x + self.cell_size - 2, y + self.cell_size - 2,
                    fill=agent.get_color(), tags="agent"
                )
            elif isinstance(agent, Mur):
                # Draw walls as rectangles
                self.canvas.create_rectangle(
                    x, y, 
                    x + self.cell_size, y + self.cell_size,
                    fill=agent.get_color(), tags="wall"
                )

    def get_gradient_color(self, intensity):
        # Convert from blue (cold) to red (hot)
        r, g, b = colorsys.hsv_to_rgb(0.7 - (intensity * 0.7), 1, intensity)
        return f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'

    def update_display(self):
        if not self.game_over:
            self.draw_agents()
        else:
            self.display_game_over()
        self.root.update()