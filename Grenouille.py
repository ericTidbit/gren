from Mouche import Mouche

class Grenouille:
    """
    Représente une grenouille
    """
    def __init__(self, longueur_langue: float, taille: int, couleur: str = "vert", longueur_saut: int = 100, position: int = 0):
        self.longueur_langue = longueur_langue
        self.taille = taille
        self.longueur_saut = longueur_saut

        self._couleur = couleur
        set_couleur(couleur)

        self._position = None
        self._position = position

    # getters
    def get_position(self) -> int:
        return self._position

    # setters
    def set_couleur(self, couleur: str) -> None:
        if couleur.lower() in ["vert", "rouge", "bleu", "jaune", "mauve"]
            self._couleur = couleur

    def set_position(self, position: int) -> None:
        self._position = position

    # methods
    def sauter(self, impulsion: int) -> None:
        """
        :param impulsion: Valeur entre 0 et 100, que détermine le pourcentage du saut
        :return: rien
        """
        pass

    def manger(self, mouche: Mouche) -> None:
        """
        Mange la mouche si elle est à portée
        Affiche un message en cas de succès ou d'échec
        :param mouche: la mouche a manger
        :return: Rien
        """
        pass

    def parler(self) -> None:
        print("Ribbit !")