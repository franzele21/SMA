# 🎮 SMA - Simulations

## 👥 Auteurs

Ce projet a été réalisé en binôme par :
- 🧑‍💻 [LAGUE Pierre]
- 👩‍💻 [MULLER François]

Dans le cadre du cours de [SMA] à [Université de Lille].

## 🚀 Déploiement / Compilation

### 🛠️ Compilation

1. Assurez-vous d'avoir Python 3.x installé sur votre système.
2. Clonez le dépôt :
   ```
   git clone https://github.com/franzele21/SMA.git
   ```
3. Naviguez vers le répertoire du projet :
   ```
   cd hunter # si vous voulez la simulation hunter
   cd particules # si vous voulez la simulation particules
   cd wator # si vous voulez la simulation wator
   ```
4. Installez les dépendances requises :
   ```
   pip install -r requirements.txt
   ```

### 🏃‍♂️ Lancement

Pour lancer la simulation, situez vous dans le dossier de la simulation en question et exécutez :
```
python Main.py
```

### ⚙️ Changement des paramètres

Les paramètres principaux se trouvent dans le fichier `config.py`. Voici quelques exemples de modifications :

1. Changer la taille de la grille ou la seed:
   ```python
   width = 20
   height = 20
   seed = 1234567
   ```

2. Modifier la densité des obstacles (hunter simulation seulement) :
   ```python
   degradation = 0.3  # 30% de la grille sera occupée par des obstacles
   ```

3. Ajuster la vitesse de la simulation :
   ```python
   pause = 0.5  # Pause de 0.5 secondes entre chaque tour
   ```

4. Ajouter le nombre d'agents dans la simulation (particules):
   ```python
   nbParticles = 100
   ```
5. Lancer la trace de la simulation (particules et wator seulement):
   ```python
   trace = True
   ```
6. Modifier la période de gestation, la limite de faim des requins ou des poissons (wator seulement):
   ```python
   gest_poisson = 2
   gest_requins = 3
   faim_requins = 6
   ```
   
## 🌟 Configurations remarquables

1. 🏞️ Labyrinthe complexe généré à l'aide de l'algorithme de Prim (simulation hunter:
   ```python
   width = 30
   height = 30
   degradation = 0.4
   ```
   Cette configuration crée un environnement de type labyrinthe, mettant à l'épreuve l'algorithme de pathfinding du Hunter.

2. 🏎️ Avatar dirigé par l'utilisateur :
   Avec les flèches "gauche", "droite", "haut", "bas", l'utilisateur peut diriger son avatar à travers la grille.
   Cette configuration offre une expérience de jeu rapide et intense avec une fenêtre de Game Over unique ! (aurez-vous le easter egg ... heheheheh ??)

3. 🧠 Test d'intelligence du Hunter :
   Un algorithme de type PathFinder A* à été implémenté pour le hunter ainsi qu'une fonction qui permet de visualiser le gradient d'optimalité du chemin prévu.
   ![image](https://github.com/user-attachments/assets/2c282e08-0587-4b6a-b409-c8e12e182610)
   Ces paramètres poussent le Hunter à calculer plus de chemins potentiels et à planifier plus loin dans le futur.

4. 🐟 Une visualisation intéressante de la simulation wator:
   Les poissons, si mis à nombre égal ou supérieur aux requins, gagnent toujout la simulation.

5. 💻 Une très bonne utilisation du package core avec une généralisation optimisée
   Dans chacune de nos simulations nous faisons appel au package core. qui représente les classes génériques de nos simulations. La classe GenericEnvironement est très complète et complètement modulable pour chacune des simulations.
   Nous avons aussi respecté le paradigme de programmation orientée objets ce qui rend le code très compréhensible.
   
## 🐛 Bugs et améliorations

### Bugs connus :

- Hunter
  - 🐞 Parfois, le Hunter peut rester bloqué dans un coin si l'Avatar est inaccessible.
  - 🐞 Dans de rares cas, la génération d'obstacles peut créer des zones inaccessibles.
  - 🐞 La génération de labyrinthe peut enferme l'Avatar.
- Wator
  - 🐛 L'environnement python ne permet pas de faire une simulation très optimisée, nous ne pouvons donc pas forcément mettre beaucoup d'agents dans la simulation.
  - 🐛 Nous n'arrivons pas à trouver le pattern de sinusoïdes d'apparition et disparition des agents.

### Améliorations futures :
- 🚀 Implémenter un mode multijoueur permettant à deux joueurs de contrôler le Hunter et l'Avatar.
- 🎨 Ajouter des thèmes visuels personnalisables pour l'environnement.
- 📊 Intégrer un système de score et de classement.
- 🧪 Créer différents types d'obstacles avec des effets variés sur le mouvement des agents.
- 🚒 Utiliser un autre type de moteur de visualisation que celui de Python pour pouvoir mettre des milliers d'agents dans wator et particules.

---

François Muller (@franzele21)
Pierre Lague (@Jakcrimson)
