# 🎮 SMA - Simulations

## 👥 Authors

This project was completed as a pair by:
- 🧑‍💻 [Pierre LAGUE]
- 👩‍💻 [François MULLER]

As part of the [SMA] course at [Université de Lille].

## 🚀 Deployment / Compilation

### 🛠️ Compilation

1. Ensure you have Python 3.x installed on your system.
2. Clone the repository:
   ```
   git clone https://github.com/franzele21/SMA.git
   ```
3. Navigate to the project directory:
   ```
   cd hunter # if you want the hunter simulation
   cd particules # if you want the particles simulation
   cd wator # if you want the wator simulation
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### 🏃‍♂️ Running

To run the simulation, navigate to the folder of the desired simulation and execute:
```
python Main.py
```

### ⚙️ Changing Parameters

The main parameters are found in the `config.py` file. Here are some examples of modifications:

1. Change the grid size or the seed:
   ```python
   width = 20
   height = 20
   seed = 1234567
   ```

2. Modify the obstacle density (hunter simulation only):
   ```python
   degradation = 0.3  # 30% of the grid will be occupied by obstacles
   ```

3. Adjust the speed of the simulation:
   ```python
   pause = 0.5  # Pause of 0.5 seconds between each round
   ```

4. Add the number of agents in the simulation (particles):
   ```python
   nbParticles = 100
   ```
5. Enable simulation trace (particles and wator only):
   ```python
   trace = True
   ```
6. Modify the gestation period, hunger limit for sharks, or for fish (wator only):
   ```python
   gest_poisson = 2
   gest_requins = 3
   faim_requins = 6
   ```

## 🌟 Notable Configurations

1. 🏞️ Complex Maze Generated Using Prim’s Algorithm (hunter simulation):
   ```python
   width = 30
   height = 30
   degradation = 0.4
   ```
   This configuration creates a maze-like environment, testing the pathfinding algorithm of the Hunter.

2. 🏎️ User-Controlled Avatar:
   Using the arrow keys ("left", "right", "up", "down"), the user can navigate their avatar through the grid.
   This configuration offers a fast-paced and intense gameplay experience with a single Game Over screen! (Will you find the Easter egg ... heheheheh ??)

3. 🧠 Hunter Intelligence Test:
   A PathFinder A* algorithm has been implemented for the Hunter along with a function to visualize the optimality gradient of the planned path.
   ![image](https://github.com/user-attachments/assets/d4e48d89-1aa3-4e1f-bf84-5c76d84dba4e)
   
   These parameters push the Hunter to calculate more potential paths and plan further into the future.

5. 🐟 An Interesting Visualization of the Wator Simulation:
   If fish are set to an equal or higher number than sharks, they will always win the simulation.

6. 💻 Excellent Use of the Core Package with Optimized Generalization:
   In each of our simulations, we use the core package, which represents the generic classes of our simulations. The `GenericEnvironment` class is very complete and fully modular for each simulation.
   We also adhered to the object-oriented programming paradigm, making the code highly understandable.

## 🐛 Bugs and Improvements

### Known Bugs:

- Hunter
  - 🐞 Sometimes, the Hunter can get stuck in a corner if the Avatar is inaccessible.
  - 🐞 In rare cases, obstacle generation can create inaccessible zones.
  - 🐞 Maze generation can trap the Avatar.
- Wator
  - 🐛 The Python environment doesn't allow for highly optimized simulations, so we can't add a large number of agents to the simulation.
  - 🐛 We haven't been able to find the sinusoidal pattern of agent appearance and disappearance.

### Future Improvements:
- 🚀 Implement a multiplayer mode allowing two players to control the Hunter and the Avatar.
- 🎨 Add customizable visual themes for the environment.
- 📊 Integrate a scoring and ranking system.
- 🧪 Create different types of obstacles with various effects on agent movement.
- 🚒 Use a different visualization engine than Python to allow for thousands of agents in the wator and particle simulations.

---

François Muller (@franzele21)
Pierre Lague (@Jakcrimson)
