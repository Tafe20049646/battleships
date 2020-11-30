from ships.Ships import Ships


class Submarine(Ships):
    name = 'Submarine'
    shape = 3

    def __init__(self):
        super().__init__()
        self.name = 'Submarine'
        self.shape = 3

    # def set_position(self, position):
    #     self.position = position


