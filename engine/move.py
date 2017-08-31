
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
            occupant = self.board.get_piece_at(pos[0], pos[1])
            if(occupant):
                if(i == self.t.magnitude-1):
                    return (self.piece.is_white != occupant.is_white)
                else:
                    return False
            if((pos[0] > 7) or (pos[1] > 7) or (pos[0] < 0) or (pos[1] < 0)):
                return False
        self.new_pos = pos
        return True

    def apply(self):
        capture = self.board.get_piece_at(self.new_pos[0], self.new_pos[1])
        if(capture):
            self.board.remove_piece_at(self.new_pos[0], self.new_pos[1])
        self.piece.set_position(self.new_pos[0], self.new_pos[1])

    def value(self):
        capture = self.board.get_piece_at(self.new_pos[0], self.new_pos[1])
        if(capture):
            return capture.value
        else:
            return 0
