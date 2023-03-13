from tkinter import *




# VARIABLES ############################################################

L = 800
H = 500

r = 70
s = 60
t = 5
x0 = x = 50
y0 = y = 50
liste_case = [0] * 42
gagnant = 0

# FONCTIONS ############################################################

def effacer():
	""" réinitialiser une partie en remettant tout à 0"""
	global liste_case, gagnant 
	can.delete(ALL)
	jeu_entier()	# tout réinitialiser
	liste_case = [0] * 42
	can.bind("<Button-3>", jeton_jaune)
	gagnant = 0


#####  Créer la grille du jeu avec 6 lignes et 7 colonnes et des trous dans chaque case #####
#############################################################################################

def ligne_de_jeu(x,y):
	""" créer une ligne de la grille pour ensuite la multiplier"""
	for i in range(0,7):
		can.create_rectangle(x, y, x + r, y + r,  fill = 'blue')
		x = x + r
		
def trou(x,y):
	""" créer les trous qui vont former la grille"""
	for i in range(0,7):
		can.create_oval(x + t, y + t , x + s + t , y + s + t , fill = 'pink') # t est une variable pour centrer les trous dans les cases
		x = x + r
	

def jeu_entier():
	""" créer la grille complète et trouée"""
	x = x0
	y = y0
	for i in range(0,6):
		ligne_de_jeu(x,y)
		trou(x,y)
		x = x0
		y = y + r
		

	
##### Créer des jetons pour jouer à deux #####
##############################################
	
def jeton_jaune(event):
	""" créer le jeton jaune"""
	i = (event.x - x0) // r		# i = numéro de la colonne
	j = (event.y - y0) // r 	# j = numéro de la ligne
	j = 5
	while liste_case[i + j * 7] != 0:
		j = j - 1 				# empecher les pions de se superposer
	x = i * r + x0
	y = j * r + y0
	can.create_oval(x + t, y + t , x + s + t , y + s + t , fill = 'yellow')
	liste_case[i + j * 7 ] = 1	# marquer la case qu'occupe le pion jaune pour montrer qu'elle est occupée par un jeton jaune
	can.unbind("<Button-3>")	# empecher le pion jaune de rejouer
	can.bind("<Button-1>", jeton_rouge)	# permettre au pion rouge de jouer
	test_victoire()



def jeton_rouge(event):
	""" créer le jeton rouge"""
	i = (event.x - x0) // r		# i = numéro de la colonne
	j = (event.y - y0) // r 	# j = numéro de la ligne
	j = 5
	while liste_case[i + j * 7] != 0:
		j = j - 1 				# empecher les pions de se superposer
	x = i * r + x0
	y = j * r + y0
	can.create_oval(x + t, y + t , x + s + t , y + s + t , fill = 'red')
	liste_case[i + j * 7 ] = 2	# marquer la case qu'occupe le pion rouge pour montrer qu'elle est occupée par un jeton rouge
	can.unbind("<Button-1>")	# empecher le pion rouge de rejouer
	can.bind("<Button-3>", jeton_jaune)	# permettre au pion jaune de jouer
	test_victoire()
	


#### Les alignements de 4 jetons possibles pour gagner#######################
#############################################################################

def victoire_horizontale():
	"""détecter que 4 jetons sont alignés horizontalement"""
	global gagnant
	for j in range(0,6):
		for i in range(0,4):
			if liste_case[i + 7 * j] == 1 and liste_case[i + 1 + 7 * j] == 1 and liste_case[i + 2 + 7 * j] == 1 and liste_case[i + 3 + 7 * j] == 1:
				gagnant = 1
			elif liste_case[i + 7 * j] == 2 and liste_case[i + 1 + 7 * j] == 2 and liste_case[i + 2 + 7 * j] == 2 and liste_case[i + 3 + 7 * j] == 2:
				gagnant = 2


def victoire_verticale():
	"""détecter que 4 jetons sont alignés verticalement"""
	global gagnant
	for i in range(0,7):
		for j in range(0,3):
			if liste_case[i + 7 * j] == 1 and liste_case[i + 7 * (j+1)] == 1 and liste_case[i + 7 * (j+2)] == 1 and liste_case[i + 7 * (j+3)] == 1:
				gagnant = 1
			elif liste_case[i + 7 * j] == 2 and liste_case[i + 7 * (j+1)] == 2 and liste_case[i + 7 * (j+2)] == 2 and liste_case[i + 7 * (j+3)] == 2:
				gagnant = 2
	
	
def victoire_diagonale_croissante():
	"""détecter que 4 jetons sont alignés en diagonale croissante"""
	global gagnant
	for i in range(0,4):
		for j in range(0,6):
			if liste_case[i + 7 * j] == 1 and liste_case[i + 1 + 7 * (j-1)] == 1 and liste_case[i + 2 + 7 * (j-2)] == 1 and liste_case[i + 3 + 7 * (j-3)] == 1:
				gagnant = 1
			elif liste_case[i + 7 * j] == 2 and liste_case[i + 1 + 7 * (j-1)] == 2 and liste_case[i + 2 + 7 * (j-2)] == 2 and liste_case[i + 3 + 7 * (j-3)] == 2:
				gagnant = 2
	
	
def victoire_diagonale_decroissante():
	"""détecter que 4 jetons sont alignés en diagonale décroissante"""
	global gagnant
	for i in range(0,4):
		for j in range(0,6):
			if liste_case[i - 7 * j] == 1 and liste_case[i + 1 - 7 * (j-1)] == 1 and liste_case[i + 2 - 7 * (j-2)] == 1 and liste_case[i + 3 - 7 * (j-3)] == 1:
				gagnant = 1
			elif liste_case[i - 7 * j] == 2 and liste_case[i + 1 - 7 * (j-1)] == 2 and liste_case[i + 2 - 7 * (j-2)] == 2 and liste_case[i + 3 - 7 * (j-3)] == 2:
				gagnant = 2
				
				
				
def victoire():
	""" définir si les jaunes ou les rouges gagnent"""
	if gagnant == 1:	#rappel: une case est marquée par un 1 quand le jeton est jaune
		print("Les jaunes ont gagné")
		can.unbind("<Button-1>")
		can.unbind("<Button-3>")
	elif gagnant == 2:	#rappel: une case est marquée par un 2 quand le jeton est rouge
		print("Les rouges ont gagné")
		can.unbind("<Button-1>")
		can.unbind("<Button-3>")	
		
		
def test_victoire():
	"""regrouper toutes les possibilités de victoire"""
	victoire_horizontale()
	victoire_verticale()
	victoire_diagonale_croissante()
	victoire_diagonale_decroissante()
	victoire()
	
	
# WIDGETS ##############################################################

	
fen = Tk()
fen.title("Puissance 4")


can = Canvas(fen, height = H, width= L, bg = 'pink')
can.pack()

tex = Label(fen, text = " Jouez pour gagner", fg = 'blue', bg = 'yellow', font = " Arial")
tex.pack()

bou0 = Button(fen, text = "quitter", command = fen.quit)
bou0.pack()


bou1 = Button(fen, text = "Nouvelle partie", command = effacer)
bou1.pack()


# Programme ############################################################





#can.bind("<Button-1>", jeton_rouge)
can.bind("<Button-3>", jeton_jaune)	# choisir de faire commencer les rouges ou les jaunes



jeu_entier()








	
fen.mainloop()
