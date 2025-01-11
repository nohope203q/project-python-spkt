class Disk:
    def __init__(self, size, isRedTop):
        self.size=size
        self.isRedTop = True

    def flip(self):
        self.isRedTop = not self.isRedTop