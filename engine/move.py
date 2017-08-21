
class Move():

    def __init__(self, board, piece, transform):
        self.board = board
        self.piece = piece
        self.t = transform

    def is_valid(self):
        pos = self.piece.get_position()
        for i in range(self.t.magnitude):
            pos[0] = pos[0]+self.t.x
            pos[1] = pos[1]+self.t.y
            if((self.board.get_piece_at(pos[0], pos[1]) != None) and (i != self.t.magnitude-1)):
                return False
            if((pos[0] > 7) or (pos[1] > 7) or (pos[0] < 0) or (pos[1] < 0)):
                return False
        self.new_pos = pos
        return True

    def apply(self):
        self.piece.set_position(self.new_pos[0], self.new_pos[1])

