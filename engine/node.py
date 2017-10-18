import copy

class Node():

    def __init__(self, parent, board, move):
        self.parent = parent
        self.move = move
        self.value = move.value()
        self.board = copy.copy(board)

    def apply(self):
        if(self.parent is not None):
            raise "Not root node."
        else:
            self.move.apply()

