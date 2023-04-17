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
canvas.pack()

# Créer la grille (une liste de listes)
states = [[color_white for col in range(grid_size)] for row in range(grid_size)]

speed_scale = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL)
speed_scale.pack()

# Créer la fourmi
ant_row = grid_size // 2
ant_col = grid_size // 2
ant_direction = "up"
running = False
step = True
speed = int(speed_scale.get())

# Définir les règles de Langton's ant
def langtons_ant():
    global ant_row, ant_col, ant_direction
    global running, step , speed
    # Si la case sur laquelle se trouve la fourmi est blanche
    if running:
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
        # Déplacer la fourmi
        if ant_direction == "up":
            ant_row -= 1
        elif ant_direction == "right":
            ant_col += 1
        elif ant_direction == "down":
            ant_row += 1
        else:
            ant_col -= 1
        # Vérifier que la fourmi ne sort pas de la grille
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

def back_langtons_ant():
    global ant_row, ant_col, ant_direction
    global running, step , speed
    # Si la case sur laquelle se trouve la fourmi est blanche
    if running:
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
        # Appeler cette fonction à nouveau après un court délai
        if step:
            canvas.after(speed, back_langtons_ant)

def reset_langtons_ant():
    global ant_row, ant_col, ant_direction, running, step
    # Reset the grid state to all white
    for row in range(grid_size):
        for col in range(grid_size):
            states[row][col] = color_white
            canvas.itemconfig(cells[row][col], fill=states[row][col])
    # Reset the ant position and direction
    ant_row = grid_size // 2
    ant_col = grid_size // 2
    ant_direction = "up"
    # Stop the simulation and reset the step mode
    running = False
    step = True

def start_langtons_ant():
    global running , step
    running = True
    step = True
    langtons_ant()

def stop_langtons_ant():
    global running
    running = False

def step_langtons_ant():
    global step , running
    step = False
    running = True
    langtons_ant()

def back_step_langtons_ant():
    global running , step
    running = True
    step = True
    back_langtons_ant()

def update_speed(*args):
    global speed
    speed = int(speed_scale.get())
speed_scale.config(command=update_speed)

def save_state():
    # Create a dictionary representing the current state
    state_dict = {
        "grid_size": grid_size,
        "states": states,
        "ant_row": ant_row,
        "ant_col": ant_col,
        "ant_direction": ant_direction
    }
    # Convert the dictionary to a JSON string
    state_json = json.dumps(state_dict)
    # Open a file dialog to get the file path to save to
    file_path = tk.filedialog.asksaveasfilename(defaultextension=".json")
    # Write the JSON string to the file
    with open(file_path, "w") as f:
        f.write(state_json)

def open_instance():
    # Open a file dialog box for the user to select the saved instance file
    filename = filedialog.askopenfilename(title="Open a saved instance", filetypes=[("JSON files", "*.json")])

    # Load the saved instance data from the selected file
    with open(filename, "r") as f:
        instance_data = json.load(f)

    # Update the states list and the ant position and direction with the loaded data
    global states, ant_row, ant_col, ant_direction
    states = instance_data["states"]
    ant_row, ant_col, ant_direction = instance_data["ant_row"], instance_data["ant_col"], instance_data["ant_direction"]

    # Update the grid on the canvas to match the updated states list
    for row in range(grid_size):
        for col in range(grid_size):
            canvas.itemconfig(cells[row][col], fill=states[row][col])

    # Start the simulation with the loaded state


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

start_button = tk.Button(root, text="start", command=start_langtons_ant)
start_button.pack()

stop_button = tk.Button(root, text="stop", command=stop_langtons_ant)
stop_button.pack()

step_button = tk.Button(root, text="step", command=step_langtons_ant)
step_button.pack()

reset_button = tk.Button(root, text="reset", command=reset_langtons_ant)
reset_button.pack()

back_button = tk.Button(root, text="back", command=back_step_langtons_ant)
back_button.pack()

save_button = tk.Button(root, text="Save", command=save_state)
save_button.pack()


# Create a "Open instance" button
open_button = tk.Button(root, text="Open instance", command=open_instance)
open_button.pack()



root.mainloop()