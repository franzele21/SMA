import tkinter as tk
from PIL import Image, ImageTk
import io
import requests
import numpy as np
class GenericEnvironment:
    def __init__(self, width, height, cell_size, torus=False):
        self.width = width
        self.height = height
        self.torus = torus
        self.mas = None  # Will be set by MAS class

        self.cell_size = cell_size
        self.canvas_width = self.width * self.cell_size
        self.canvas_height = self.height * self.cell_size

        self.root = tk.Tk()
        self.root.title("Multi-Agent System Simulation")
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, background="black")
        self.canvas.pack()

        self.game_over = False
        self.game_over_image = None

    def draw_grid(self):
        for i in range(0, self.canvas_width, self.cell_size):
            self.canvas.create_line(i, 0, i, self.canvas_height)
        for i in range(0, self.canvas_height, self.cell_size):
            self.canvas.create_line(0, i, self.canvas_width, i)

    def draw_agents(self):
        self.canvas.delete("agent")
        for agent in self.mas.agent_list:
            x = agent.pos_x * self.cell_size
            y = agent.pos_y * self.cell_size
            self.canvas.create_oval(x, y, x + self.cell_size, y + self.cell_size, fill=agent.get_color(), tags="agent")

    def update_display(self):
        if not self.game_over:
            self.draw_agents()
        else:
            self.display_game_over()
        self.root.update()

    def load_game_over_image(self, url):
        response = requests.get(url)
        img = Image.open(io.BytesIO(response.content))
        img = img.resize((self.canvas_width, self.canvas_height), Image.LANCZOS)
        self.game_over_image = ImageTk.PhotoImage(img)

    def display_game_over(self):
        RAHHH = np.random.rand()
        if RAHHH < 0.5:
            if not self.game_over_image:
                self.load_game_over_image("https://media1.tenor.com/m/aSkdq3IU0g0AAAAC/laughing-cat.gif")  # Replace with actual image URL
        
        else:
            if not self.game_over_image:
                self.load_game_over_image("https://steamuserimages-a.akamaihd.net/ugc/368532758831917241/3BE6BAFA32473CC1B09E2C015F75ACAFB6626852/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true")  # Replace with actual image URL
            
        if self.game_over_image:
            self.canvas.delete("all")
            self.canvas.create_image(self.canvas_width // 2, self.canvas_height // 2, image=self.game_over_image)

    def run_gui(self):
        self.draw_grid()
        self.root.mainloop()