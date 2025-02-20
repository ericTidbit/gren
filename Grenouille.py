from Mouche import Mouche

class Grenouille:
    """
    Représente une grenouille
    """
    def __init__(self, longueur_langue: float, taille: int, poids: float, longueur_saut: int, couleur: str = "vert", position: int = 0):
        self.longueur_langue = longueur_langue
        self.longueur_saut = longueur_saut

        self.poids = poids

        self._taille = None
        self.set_taille(taille)

        self._couleur = couleur

        self._position = None
        self.set_position(position)

    # getters
    def get_poids(self) -> float:
        return self.poids

    def get_taille(self) -> int:
        return self._taille

    def get_couleur(self) -> str:
        return self._couleur

    def get_position(self) -> int:
        return self._position

    # setters
    def set_poids(self, poids: float) -> None:
        if poids > 0:
            self.poids = poids
        else:
            raise ValueError("Poids doit être positif et plus grand que 0")

    def set_taille(self, taille: int) -> None:
        if taille >= 1:
            self._taille = taille
        else:
            raise ValueError("La taille de la grenouille doit être plus grande ou égale à 1 cm")

    def set_position(self, position: int) -> None:
        if position >= 0:
            self._position = position
        else:
            raise ValueError("La position doit être positive")

    # methods
    def sauter(self, impulsion: int) -> None:
        """
        :param impulsion: Valeur entre 0 et 100, que détermine le pourcentage du saut
        :return: rien
        """
        if 0 <= impulsion <= 100:
            self._position = self.longueur_saut * impulsion / 100
        else:
            raise ValueError("Impulsion doit être entre 0 et 100")

    def manger(self, mouche: Mouche) -> None:
        """
        Mange la mouche si elle est à portée
        Affiche un message en cas de succès ou d'échec
        :param mouche: la mouche a manger
        :return: Rien
        """
        if abs(self._position - mouche.get_position()) <= self.longueur_langue:
            self.set_poids(self.poids + mouche.get_poids())
            print("La grenouille mange la mouche!")
        else:
            print("La grenouille ne mange pas la mouche!")

    def parler(self) -> None:
        print("Ribbit !")

    def __str__(self):
        return f"Une grenouille de {self.poids} grammes et {self._taille} cm."