
class Move():

    # TODO: This is ugly
    FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def __init__(self, board, piece, transform):
        self.board = board
        self.piece = piece
        self.t = transform
        self.is_capture = False

    def str(self):
        move_str = self.piece.str()
        if(self.is_capture):
            move_str = move_str+'x'
        move_str = move_str+self.FILES[self.new_pos[0]]
        move_str = move_str+str(self.new_pos[1]+1)
        return move_str

    # TODO: Fix this - violates SRP
    # Must be called first - calculates new_pos
    def is_valid(self):
        pos = self.piece.get_position()
        is_valid = True
        for i in range(self.t.magnitude):
            pos[0] = pos[0]+self.t.x
            pos[1] = pos[1]+self.t.y
            occupant = self.board.get_piece_at(pos[0], pos[1])
            if(occupant):
                if(i == self.t.magnitude-1):
                    capture = (self.piece.is_white != occupant.is_white)
                    self.is_capture = capture
                    is_valid = capture
                else:
                    is_valid = False
                break
            if((pos[0] > 7) or (pos[1] > 7) or (pos[0] < 0) or (pos[1] < 0)):
                is_valid = False
        if(is_valid):
            self.new_pos = pos
        return is_valid

    def apply(self):
        if(self.is_capture):
            self.board.remove_piece_at(self.new_pos[0], self.new_pos[1])
        self.piece.set_position(self.new_pos[0], self.new_pos[1])

    def value(self):
        if(self.is_capture):
            return self.board.get_piece_at(self.new_pos[0], self.new_pos[1]).value
        else:
            return 0
