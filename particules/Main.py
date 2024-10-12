from Environnement import Environment
from MAS import MAS
import json
import os

def read_config(file_path):
    try:
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
        
        # Validate and set default values if needed
        config['width'] = int(config.get('width', 800))
        config['height'] = int(config.get('height', 600))
        config['view'] = config.get('view', {})
        config['view']['boxSize'] = int(config['view'].get('boxSize', 10))
        config['nbTicks'] = int(config.get('nbTicks', 0))
        config['nbParticles'] = int(config.get('nbParticles', 100))
        config['pause'] = float(config.get('pause', 0.1))
        config['seed'] = int(config.get('seed', 0))
        config['trace'] = bool(config.get('trace', False))
        
        return config
    except FileNotFoundError:
        print(f"Configuration file not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON in configuration file: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading configuration file: {e}")
        return None



def main():
    config = read_config(os.path.join(".", "config.json"))
    print(config)
    w = config['width']
    h = config['height']
    nb_agents = config['nbParticles']
    num_turns = config["nbTicks"]
    trace = config["trace"]
    cell_size = config["view"]["boxSize"]
    seed = config["seed"]
    env = Environment(w, h, cell_size, torus=False)
    mas = MAS(env, nb_agents, seed, trace)
    mas.run_simulation(num_turns)
    env.run_gui()

if __name__ == "__main__":
    main()