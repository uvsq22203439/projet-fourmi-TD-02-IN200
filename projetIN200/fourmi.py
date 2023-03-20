#Importation des modules
from tkinter import * 
from random import randrange 
from time import * 





#Paramétrage de la fenêtre et créations des variables
L = 900
H = 900

liste_cases = []

# Fonctions 
def quadrillage(x,y):
	""" créer le quadrillage qui sera l'environnement de déplacement de la fourmi """
	for i in range(9):
		for j in range(9):
			can.create_rectangle(x,y, x+ 100, y+ 100,  fill = 'white')
			x+= 100
			liste_cases.append(1)
		y = y +100
		x = 0
		print(liste_cases)
	
def fourmi():
	can.create_line(L/2-20,H/2,(L/2-20)+40,H/2, arrow = 'last',width = 2)
	
	
	
def play():
	quadrillage(0,0)
	fourmi()
	
def pause():
	pass
	
def suivant():
	pass



		



#Paramètres de la fenêtre Tkinter	
fen = Tk()
fen.title("Fourmi de Langton")
tex = Label(fen, text = "Fourmi de Langton.", fg = 'purple', bg = 'white', font = "arial 20")
tex.grid(column = 1, row = 1)

can = Canvas(fen, height = H,width = L,bg = 'grey')
can.grid(column = 1, rowspan = 4)

bou0 = Button(fen, text = 'play', command = play)
bou0.grid(column = 2, row = 2)

bou1 = Button(fen, text = 'pause', command = pause)
bou1.grid(column = 2, row = 3)

bou2 = Button(fen, text = 'next', command = suivant)
bou2.grid(column = 2, row = 4)




fen.mainloop()
