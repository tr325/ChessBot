
class Move():

    # TODO: This is ugly
    FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def __init__(self, piece, transform):
        self.piece = piece
        self.original_position = piece.get_position()
        self.t = transform
        self.is_capture = False
        self.captured_piece = None

    def str(self):
        move_str = ""
        if(self.piece.str().upper() == "P"):
            if(self.is_capture):
                move_str = 'x'
        else:
            move_str = self.piece.str()
            if(self.is_capture):
                move_str = move_str+'x'
            else:
                move_str = move_str+' '
        move_str = move_str+self.FILES[self.new_pos[0]]
        move_str = move_str+str(self.new_pos[1]+1)
        return move_str

    # TODO: Fix this - violates SRP
    # Must be called first - calculates new_pos
    def is_valid(self, board):
        pos = self.piece.get_position()
        is_valid = True
        for i in range(self.t.magnitude):
            pos[0] = pos[0]+self.t.x
            pos[1] = pos[1]+self.t.y
            occupant = board.get_piece_at(pos[0], pos[1])
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
        self.is_valid = is_valid
        return is_valid

    def apply(self, board):
        if(not self.is_valid):
            raise Exception("Cannot apply an invalid move")
        if(self.is_capture):
            self.captured_piece = board.get_piece_at(self.new_pos[0], self.new_pos[1])
            board.remove_piece_at(self.new_pos[0], self.new_pos[1])
        self.piece.set_position(self.new_pos[0], self.new_pos[1])
        board.change_turn()

    def undo(self, board):
        if(self.captured_piece is not None):
            board.pieces.append(self.captured_piece)
        self.piece.set_position(self.original_position[0], self.original_position[1])
        # changing turn forwards and backwards is equivalent
        board.change_turn()

    def value(self, board):
        if(self.is_capture):
            return board.get_piece_at(self.new_pos[0], self.new_pos[1]).value
        else:
            return 0
