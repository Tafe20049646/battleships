from ships.Ships import Ships


class PatrolBoat(Ships):
    name = 'Patrol Boat'
    shape = 1

    def __init__(self):
        super().__init__()
        self.name = 'Patrol Boat'
        self.shape = 1

    # def set_position(self, position):
    #     self.position = position
