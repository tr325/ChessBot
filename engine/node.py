import copy

class Node():

    def __init__(self, parent, board, move):
        self.parent = parent
        self.board = copy.copy(board)
        if(parent is None):
            self.depth = 1
        else:
            self.depth = parent.depth + 1
        self.move = move
        self.value = move.value(self.board)
        self.move.apply(self.board)

