import tkinter as tk

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

# Créer la fourmi
ant_row = grid_size // 2
ant_col = grid_size // 2
ant_direction = "up"
running = False


# Définir les règles de Langton's ant
def langtons_ant():
    global ant_row, ant_col, ant_direction
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
        canvas.after(10, langtons_ant)
    else:
        pass

def start_langtons_ant():
    global running
    running = True
    langtons_ant()

def stop_langtons_ant():
    global running
    running = False

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


root.mainloop()

