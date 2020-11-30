from ships.Ships import Ships


class Battleship(Ships):

    def __init__(self):
        super().__init__()
        self.name = 'Battleship'
        self.shape = 4

    # def set_position(self, position):
    #     self.position = position
