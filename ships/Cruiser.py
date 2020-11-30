from ships.Ships import Ships


class Cruiser(Ships):
    name = 'Cruiser'
    shape = 3

    def __init__(self):
        super().__init__()
        self.name = 'Cruiser'
        self.shape = 3

    # def set_position(self, position):
    #     self.position = position
