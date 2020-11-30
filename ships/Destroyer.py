from ships.Ships import Ships


class Destroyer(Ships):
    name = 'Destroyer'
    shape = 2

    def __init__(self):
        super().__init__()
        self.name = 'Destroyer'
        self.shape = 2

    # def set_position(self, position):
    #     self.position = position
