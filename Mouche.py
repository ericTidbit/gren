class Mouche:
    def __init__(self, poids: int, position: int = 0):
        self._poids = None
        self.set_poids(poids)

        self._position = None
        self.set_position(position)

    def get_poids(self):
        return self._poids

    def get_position(self) -> int:
        return self._position

    def set_poids(self, poids: int):
        if poids >= 0:
            self._poids = poids
        else:
            raise ValueError("Poids doit être plus grand que 0")

    def set_position(self, new_position):
        if new_position >= 0:
            self._position = new_position