# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	def __init__(self, robot=(0,0), sortie=(0,0), obstacles={}, hauteur=0, largeur=0):

		self.robot = robot
		self.sortie = sortie
		self.obstacles = obstacles
		self.hauteur = hauteur
		self.largeur = largeur


	def transforme_coordonnees_index(self,point,largeur):
		return point[0]*(largeur+2)+point[1]

	def __repr__(self):
		
		s = [" "]*(self.hauteur * (self.largeur + 2))

		for obstacle in self.obstacles:
			s[self.transforme_coordonnees_index(obstacle,self.largeur)] = self.obstacles[obstacle]

		for x in range(0,self.hauteur-1):
 
			s[self.largeur + x*(self.largeur+2)] = '\r'
			s[self.largeur + 1 + x*(self.largeur+2)] = '\n'

		s[self.transforme_coordonnees_index(self.robot,self.largeur)] = 'X'
		s[self.transforme_coordonnees_index(self.sortie,self.largeur)] = 'U'

		to_return = "".join(s)
		return to_return

	def fini(self):

		if (self.robot == self.sortie):
			return True
		else:
			return False

	@classmethod
	def creer_labyrinthe_depuis_chaine(cls,chaine):

		"""Initialize data from a chain"""

		obstacles = {}
		sortie = (0,0)
		robot = (0,0)
		
		ligne = 0
		colonne = 0
		largeur = 0
		last_read_char = ""

		for i, char in enumerate(chaine):

			if (char == 'O'):
				obstacles[(ligne,colonne)] = char
				colonne += 1
				
			elif (char == '.'):
				obstacles[(ligne,colonne)] = char
				colonne += 1
			
			elif (char == 'U'):
				sortie = (ligne,colonne)
				colonne += 1

			elif (char == 'X'):
				robot = (ligne,colonne)
				colonne += 1

			elif (char == '\n'):
				ligne += 1

				if (last_read_char == '\r'):
					largeur = colonne - 1
				else:
					largeur = colonne

				colonne = 0

			else:
				colonne += 1


			last_read_char = char
		
		ligne += 1

		print "on a trouve {0} lignes et {1} colonnes".format(ligne,largeur)
		return cls(robot, sortie, obstacles, ligne, largeur)
