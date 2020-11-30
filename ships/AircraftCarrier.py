from ships.Ships import Ships


class AircraftCarrier(Ships):

    def __init__(self):
        super().__init__()
        self.name = 'Aircraft Carrier'
        self.shape = 5

    # def set_position(self, position):
    #     self.position = position
