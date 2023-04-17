import tkinter as tk
import numpy as np
from random import randrange

taille_grille = 100
taille_case = 5
iterations = 10000
delai = 50
couleur_quadrillage = "lightgray"

directions = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])


def couleur_case():
    global a 
    a = randrange(3)
    if a == 1:
        a = 'white'
    else:
        a = 'black'
    return a 
    print(a)


def tourner_gauche(direction):
    return (direction - 1) % 4

def tourner_droite(direction):
    return (direction + 1) % 4

def lancer_fourmi():
    bouton_lancer.config(state=tk.DISABLED)
    bouton_recommencer.config(state=tk.DISABLED)
    fourmi_langton(0)
    bouton_lancer.config(state=tk.NORMAL)
    bouton_recommencer.config(state=tk.NORMAL)

def recommencer():
    global a 
    global case_ids
    for i in range(taille_grille):
        for j in range(taille_grille):
            canvas.itemconfig(case_ids[i, j], fill="white")
    bouton_lancer.config(state=tk.NORMAL)

def quitter():
    fenetre.destroy()

def fourmi_langton(iteration):
    global grille, position, direction
    if iteration < iterations:
        x, y = position

        if grille[tuple(position)]:
            direction = tourner_gauche(direction)
            color = "white"
        else:
            direction = tourner_droite(direction)
            color = "black"

        grille[tuple(position)] = 1 - grille[tuple(position)]
        canvas.itemconfig(case_ids[x, y], fill=color)

        position += directions[direction]
        position %= taille_grille

        fenetre.after(delai, fourmi_langton, iteration + 1)

grille = np.zeros((taille_grille, taille_grille), dtype=int)
position = np.array([taille_grille // 2, taille_grille // 2])
direction = 0

fenetre = tk.Tk()
fenetre.title("Fourmi de Langton")

canvas = tk.Canvas(fenetre, width=taille_grille * taille_case, height=taille_grille * taille_case, bg="white")
canvas.pack()

case_ids = np.empty((taille_grille, taille_grille), dtype=int)

for i in range(taille_grille):
    for j in range(taille_grille):
        case_ids[i, j] = canvas.create_rectangle(j * taille_case, i * taille_case,
                                                 (j + 1) * taille_case, (i + 1) * taille_case,
                                                 fill="white", outline=couleur_quadrillage)

bouton_frame = tk.Frame(fenetre)
bouton_frame.pack(pady=10)

bouton_lancer = tk.Button(bouton_frame, text="Lancer", command=lancer_fourmi)
bouton_lancer.pack(side=tk.LEFT, padx=5)

bouton_recommencer = tk.Button(bouton_frame, text="Recommencer", command=recommencer)
bouton_recommencer.pack(side=tk.LEFT, padx=5)

bouton_quitter = tk.Button(bouton_frame, text="Quitter", command=quitter)
bouton_quitter.pack(side=tk.LEFT, padx=5)

fenetre.mainloop()