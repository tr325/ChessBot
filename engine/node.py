
class Node():

    def __init__(self, parent, move):
        self.parent = parent
        self.move = move
        self.value = move.value()

    def apply(self):
        if(self.parent is not None):
            raise "Not root node."
        else:
            self.move.apply()

