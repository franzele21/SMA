import tkinter as tk

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
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, background="blue")
        self.canvas.pack()

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
        self.draw_agents()
        self.root.update()

    def run_gui(self):
        self.draw_grid()
        self.root.mainloop()