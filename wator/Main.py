from Environnement import Environment
from MAS import MAS
import json
import os


def read_config(file_path):
    """
Used to read the configuration file.

Parameters:
-----------
file_path <str>: The path to the configuration file.

Returns:
--------
config <dict>: All the configuration.

Notes:
------
The json file must have this format:
{
    "width": <int>,
    "height": <int>,
    "view": {
      "boxSize": <int>
    },
    "nbTicks": <int>,
    "poisson": {
        "nbpoisson" : <int>,
        "gest_poisson" : <int> 
    } ,
    "requin": {
        "nbrequin":<int>,
        "gest_requin":<int>,
        "faim_requin":<int>
    },
    "pause": <int>,
    "seed": <int>,
    "trace": <bool>
  }
    """
    try:
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
        
        # Validate and set default values if needed
        config['width'] = int(config.get('width', 800))
        config['height'] = int(config.get('height', 600))
        config['view'] = config.get('view', {})
        config['view']['boxSize'] = int(config['view'].get('boxSize', 10))
        config['nbTicks'] = int(config.get('nbTicks', 0))
        config['poisson']["nbpoisson"] = int(config["poisson"].get('nbpoisson', 5))
        config['poisson']["gest_poisson"] = int(config["poisson"].get('gest_poisson', 5))
        config['requin']["nbrequin"] = int(config["requin"].get('nbrequin', 1))
        config['requin']["gest_requin"] = int(config["requin"].get('gest_requin', 1))
        config['requin']["faim_requin"] = int(config["requin"].get('faim_requin', 1))
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
    nb_poissons = config['poisson']['nbpoisson']
    gest_poissons = config["poisson"]["gest_poisson"]
    nb_requins = config["requin"]["nbrequin"]
    gest_requins = config["requin"]["gest_requin"]
    faim_requins = config["requin"]["faim_requin"]
    num_turns = config["nbTicks"]
    trace = config["trace"]
    cell_size = config["view"]["boxSize"]
    pause = config["pause"]
    seed = config["seed"]

    print(nb_requins)
    env = Environment(w, h, cell_size, torus=False)
    mas = MAS(env, nb_poissons, nb_requins, gest_poissons, gest_requins, faim_requins, seed, pause, trace)
    mas.run_simulation(num_turns)
    env.run_gui()

if __name__ == "__main__":
    main()