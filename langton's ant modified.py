import tkinter as tk
import json
from tkinter import filedialog

# Taille de la grille (100x100)
grid_size = 100

# Couleur de chaque état
color_white = "#FFFFFF"  # blanc
color_black = "#000000"  # noir

# Créer la fenêtre principale
root = tk.Tk()
root.title("Langton's ant")

# Créer un canvas pour dessiner la grille
canvas = tk.Canvas(root, width=grid_size*5, height=grid_size*5)
canvas.grid(column = 1, rowspan = 10)

# Créer la grille (une liste de listes)
states = [[color_white for col in range(grid_size)] for row in range(grid_size)]

speed_scale = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL)
speed_scale.grid(column = 2, row = 8)

# Créer la fourmi
ant_row = grid_size // 2
ant_col = grid_size // 2
ant_direction = "up"
running = False
step = True
back = False
speed = int(speed_scale.get())

# Définir les règles de Langton's ant
def langtons_ant():
    global ant_row, ant_col, ant_direction
    global running, step , speed , back
    if running:
        if back :
            # Déplacer la fourmi
            if ant_direction == "up":
                ant_row += 1
            elif ant_direction == "right":
                ant_col -= 1
            elif ant_direction == "down":
                ant_row -= 1
            else:
                ant_col += 1
            # Vérifier que la fourmi ne sort pas de la grille
            if ant_row < 0:
                ant_row = grid_size - 1
            elif ant_row >= grid_size:
                ant_row = 0
            if ant_col < 0:
                ant_col = grid_size - 1
            elif ant_col >= grid_size:
                ant_col = 0
        # Si la case sur laquelle se trouve la fourmi est blanche
        if states[ant_row][ant_col] == color_white:
            # Tourner à droite
            if ant_direction == "up":
                ant_direction = "right"
            elif ant_direction == "right":
                ant_direction = "down"
            elif ant_direction == "down":
                ant_direction = "left"
            else:
                ant_direction = "up"
            # Changer la couleur de la case en noir
            states[ant_row][ant_col] = color_black
        # Si la case sur laquelle se trouve la fourmi est noire
        else:
            # Tourner à gauche
            if ant_direction == "up":
                ant_direction = "left"
            elif ant_direction == "right":
                ant_direction = "up"
            elif ant_direction == "down":
                ant_direction = "right"
            else:
                ant_direction = "down"
            # Changer la couleur de la case en blanc
            states[ant_row][ant_col] = color_white
        # Mettre à jour la couleur de la case dans l'interface graphique
        canvas.itemconfig(cells[ant_row][ant_col], fill=states[ant_row][ant_col])
        if not back:
            # Déplacer la fourmi
            if ant_direction == "up":
                ant_row -= 1
            elif ant_direction == "right":
                ant_col += 1
            elif ant_direction == "down":
                ant_row += 1
            else:
                ant_col -= 1
            # Vérifier que la fourmi ne sorte pas de la grille
            if ant_row < 0:
                ant_row = grid_size - 1
            elif ant_row >= grid_size:
                ant_row = 0
            if ant_col < 0:
                ant_col = grid_size - 1
            elif ant_col >= grid_size:
                ant_col = 0
            # Appeler cette fonction à nouveau après un court délai
            if step:
                canvas.after(speed, langtons_ant)        

def reset_langtons_ant():
    global ant_row, ant_col, ant_direction, running, step, back
    # Remet les cases de la grille en blanc 
    for row in range(grid_size):
        for col in range(grid_size):
            states[row][col] = color_white
            canvas.itemconfig(cells[row][col], fill=states[row][col])
    # Reinitialise la position et la direction de la fourmi
    ant_row = grid_size // 2
    ant_col = grid_size // 2
    ant_direction = "up"
    # Arrete le jeu et reinitialise la variable "step"
    running = False
    step = True
    back = False

def start_langtons_ant():
    global running , step, back
    running = True
    step = True
    back= False
    langtons_ant()

def stop_langtons_ant():
    global running
    running = False

def step_langtons_ant():
    global step , running, back
    step = False
    running = True
    back = False
    langtons_ant()

def back_step_langtons_ant():
    global running , step, back
    running = True
    back = True
    langtons_ant()

def update_speed(*args):
    global speed
    speed = int(speed_scale.get())
speed_scale.config(command=update_speed)

def save_state():
    # Créer un dictionnaire qui répertorie les différents états du jeu pour pouvoir sauvegarder une instance
    state_dict = {
        "grid_size": grid_size,
        "states": states,
        "ant_row": ant_row,
        "ant_col": ant_col,
        "ant_direction": ant_direction
    }
    # Converti le dictionnaire en  JSON
    state_json = json.dumps(state_dict)
    # Ouvre l'explorateur de fichier pour enregistrer une partie
    file_path = tk.filedialog.asksaveasfilename(defaultextension=".json")
    # Ecrit la chaine de caractère JSON dansd le fichier 
    with open(file_path, "w") as f:
        f.write(state_json)

def open_instance():
    # Ouvre l'explorateur de fichier pour ouvrir une partie sauvegardée 
    filename = filedialog.askopenfilename(title="Open a saved instance", filetypes=[("JSON files", "*.json")])

    # Charge les données d'une partie depuis un fichier enregistré
    with open(filename, "r") as f:
        instance_data = json.load(f)

    # Met à jour les variables principales 
    global states, ant_row, ant_col, ant_direction
    states, ant_row, ant_col, ant_direction = instance_data["states"], instance_data["ant_row"], instance_data["ant_col"], instance_data["ant_direction"]

    # met à jour le canevas pour qu'il corresponde aux nouvelles variables
    for row in range(grid_size):
        for col in range(grid_size):
            canvas.itemconfig(cells[row][col], fill=states[row][col])



# Créer les cases dans le canvas
cells = []
for row in range(grid_size):
    row_cells = []
    for col in range(grid_size):
        x1 = col * 5
        y1 = row * 5
        x2 = x1 + 5
        y2 = y1 + 5
        cell = canvas.create_rectangle(x1, y1, x2, y2, fill=states[row][col], outline="")
        row_cells.append(cell)
    cells.append(row_cells)

# Création et ajout des boutons dans le canevas    
start_button = tk.Button(root, text="start", command=start_langtons_ant)
start_button.grid(column = 2, row = 1)

stop_button = tk.Button(root, text="stop", command=stop_langtons_ant)
stop_button.grid(column = 2, row = 2)

step_button = tk.Button(root, text="step", command=step_langtons_ant)
step_button.grid(column = 2, row = 3)

reset_button = tk.Button(root, text="reset", command=reset_langtons_ant)
reset_button.grid(column = 2, row = 4)

back_button = tk.Button(root, text="back", command=back_step_langtons_ant)
back_button.grid(column = 2, row = 5)

save_button = tk.Button(root, text="Save", command=save_state)
save_button.grid(column = 2, row = 6)

open_button = tk.Button(root, text="Open instance", command=open_instance)
open_button.grid(column = 2, row = 7)


# Fonction permettant de maintenir la fenêtre Tkinter ouverte
root.mainloop()
