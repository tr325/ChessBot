from transform import Transform as T
from move import Move

class Piece():
    display_as = "x" # Overwrite in child classes
    has_moved = False # For Castling and Pawns
    
    # More natural to create pieces with blank constructor for white,
    # Code is more natural checking for "whiteness" first
    def __init__(self, x, y, is_black=False):
        self.is_white = not is_black
        self.x = x
        self.y = y
        
    def get_position(self):
        return [self.x, self.y]

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def is_at(self, x, y):
        return ((self.x == x) and (self.y == y))

    def str(self):
        if(self.is_white):
            return self.display_as.upper()
        else:
            return self.display_as

    def get_valid_moves(self, board):
        return False

#####################
class Pawn(Piece):
    display_as = "p"

    #TODO: en passant
    def get_valid_moves(self, board):
        moves = []
        moves.append(Move(board, self, T(0,1,1)))
        if(not self.has_moved):
            moves.append(Move(board, self, T(0,1,2)))
        if(board.get_piece_at(self.position.x+1, self.position.y+1) != None):
            moves.append(Move(board, self, T(1,1,1)))
        if(board.get_piece_at(self.position.x-1, self.position.y+1 != None)):
            moves,append(Move(board, self, T(-1,1,1)))
        valid = []
        for i in range(moves.length):
            if(moves[i].is_valid()):
                valid.append(moves[i])
        return valid

class Rook(Piece):
    display_as = "r"

class Bishop(Piece):
    display_as = "b"

class Knight(Piece):
    display_as = "n"

class Queen(Piece):
    display_as = "q"

class King(Piece):
    display_as = "k"
