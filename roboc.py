# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from labyrinthe import *
from carte import Carte

# On charge les cartes existantes
cartes = []

# Boucle pour trouver les cartes
for nom_fichier in os.listdir("cartes"):
	if nom_fichier.endswith(".txt"):
		chemin = os.path.join("cartes", nom_fichier)
		nom_carte = nom_fichier[:-4].lower()
		with open(chemin, "r") as fichier:
			contenu = fichier.read()
			# Création d'une carte, à compléter
			carte = Carte(nom_carte,contenu)
			cartes.append(carte)

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
	print("  {0} - {1}".format(i + 1, carte.nom))
	#print("{0}".format(carte.labyrinthe))

# On propose de choisir
try:
	mode=int(raw_input('Votre choix:'))
	carte = cartes[mode-1]
	print("{0}".format(carte.labyrinthe))
	fini = False

	while(fini == False):
		deplacement=raw_input('Votre deplacement:')
		deplacement = deplacement.lower()

		new_robot = carte.labyrinthe.robot

		if (deplacement == 's'):
			new_robot = (new_robot[0]+1,new_robot[1])
		elif (deplacement == 'n'):
			new_robot = (new_robot[0]-1,new_robot[1])	
		elif (deplacement == 'o'):
			new_robot = (new_robot[0],new_robot[1]-1)
		elif (deplacement == 'e'):
			new_robot = (new_robot[0],new_robot[1]+1)
		
		if (new_robot in carte.labyrinthe.obstacles):
			if (carte.labyrinthe.obstacles[new_robot] == 'O'):
				raise RuntimeError

		elif (new_robot == carte.labyrinthe.sortie):
			fini = True

		carte.labyrinthe.robot = new_robot
		print("{0}".format(carte.labyrinthe))
		

	print "########################"
	print "congrats!!! vous avez reussi a finir le labyrinthe"
	print "########################"

except KeyboardInterrupt:
	print "\nOK, on quite le jeu"

except RuntimeError:
	print "Deplacement invalide, c'est un mur... vous avez perdu"

except ValueError:
	print "Not a number"

except IndexError:
	print "Ce choix n'existe pas"

