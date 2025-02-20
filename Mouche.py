class Mouche:
    def __init__(self, position: int = 0):
        self._position = position

    def get_position(self) -> int:
        return self._position

    def set_position(self, new_position):
        if new_position >= 0:
            self._position = new_position