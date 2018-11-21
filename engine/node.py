
class Node():

    def __init__(self, parent, board, move):
        self.parent = parent
        if(parent is None):
            self.depth = 1
        else:
            self.depth = parent.depth + 1
        self.move = move
        self.value = move.value(board)
        self.move.apply(board)

