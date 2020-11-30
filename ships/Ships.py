class Ships:

    def __init__(self):
        self.status = True
        self.name = ''
        self.shape = 0
        self.position = []
        pass

    def set_position(self, position):
        self.position = position
        pass

    def hit(self):
        self.status = False


