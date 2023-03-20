import numpy as np
import matplotlib.pyplot as plt
matplotlib inline

f=np.zeros((150,150)) # On crée la grille avec toutes ses cases blanches initialement
c=np.array([[0,1],[1,0],[0,-1],[-1,0]]) # On crée le vecteur de toutes les orentations possibles de la fourmis
i,j=75,75 # Condition initiale: La fourmis est au milieu de la grille
d=1 # On crée un entier d qui représente l'index de l'orientation courante de la fourmis. Ainsi l'orientation de la 
# fourmis est c[d,:], ici c[1,:]=[1,0] elle a donc bien la tête en haut.
ts=0 # On va enregistrer le nombre de pas total cumulé
pos=np.zeros((20000,2)) # Vecteur position 

def step(n):  
    global f,i,j,d,c,ts
    for t in range(n):
        ts+=1
        d=int(np.mod(d+2*f[i,j]-1,4)) # On calcul la nouvelle orientation
        i+=c[d,0] # On avance dans
        j+=c[d,1] # la direction correspondante
        pos[ts,:]=[i,j]
        f[i,j]=np.mod(f[i,j]+1,2) # Et on change la couleur en partant !
