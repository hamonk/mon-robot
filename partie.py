# -*-coding:Utf-8 -*
from carte import *

"""Ce module contient la classe Partie."""

class Partie:

    """Objet de liaison entre une carte et un fichier de sauvegarde."""

    def __init__(self, carte, timestamp, fichier):
        self.carte = carte
        self.derniere_sauvegarde = timestamp
        self.fichier = fichier

    def __repr__(self):
        return "<Partie {0} (sauvegarde a {1})>".format(self.carte,self.timestamp)
