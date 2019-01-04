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
        self.valid_moves = []
        
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

    def _moves_in_direction(self, board, direction):
        moves = []
        for i in range(8):
            moves.append(Move(self, T(direction[0], direction[1], i+1)))
        return moves

    def _append_valid_move(self, board, move):
        if(move.is_valid(board)):
            self.valid_moves.append(move)

#### Concrete piece classes
class Pawn(Piece):
    display_as = "p"
    value = 1

    def _magnitude(self):
        if(self.is_white):
            return 1
        else:
            return -1

    #TODO: en passant
    def get_valid_moves(self, board):
        m = self._magnitude()
        if(board.get_piece_at(self.x, self.y+m) == None):
            self._append_valid_move(board, Move(self, T(0,m,1)))
        if(not self.has_moved):
            self._append_valid_move(board, Move(self, T(0,m,2)))
        if(board.get_piece_at(self.x+1, self.y+m) != None):
            self._append_valid_move(board, Move(self, T(1,m,1)))
        if(board.get_piece_at(self.x-1, self.y+m) != None):
            self._append_valid_move(board, Move(self, T(-1,m,1)))
        return self.valid_moves

class Rook(Piece):
    display_as = "r"
    value = 5

    def get_valid_moves(self, board):
        moves = []
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        for dir in directions:
            moves.extend(self._moves_in_direction(board, dir))
        for move in moves:
            self._append_valid_move(board, move)
        return self.valid_moves

class Bishop(Piece):
    display_as = "b"
    value = 3

    def get_valid_moves(self, board):
        moves = []
        directions = [[1,1],[1,-1],[-1,1],[-1,-1]]
        for dir in directions:
            moves.extend(self._moves_in_direction(board, dir))
        for move in moves:
            self._append_valid_move(board, move)
        return self.valid_moves

class Knight(Piece):
    display_as = "n"
    value = 3

    def get_valid_moves(self, board):
        transforms = [T(1,2,1), T(2,1,1), T(2,-1,1), T(1,-2,1), T(-1,-2,1), T(-2,-1,1), T(-2,1,1), T(-1,2,1)]
        for t in transforms:
            self._append_valid_move(board, Move(self, t))
        return self.valid_moves

class Queen(Piece):
    display_as = "q"
    value = 9

    def get_valid_moves(self, board):
        moves = []
        directions = [[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]]
        for dir in directions:
            moves.extend(self._moves_in_direction(board, dir))
        for move in moves:
            self._append_valid_move(board, move)
        return self.valid_moves

class King(Piece):
    display_as = "k"
    value = 1000000 #TODO: Do check and checkmate properly

    #TODO: castling
    def get_valid_moves(self, board):
        moves = []
        transforms = [T(1,1,1),T(1,-1,1),T(-1,1,1),T(-1,-1,1),T(0,1,1),T(0,-1,1),T(1,0,1),T(-1,0,1)]
        for t in transforms:
            self._append_valid_move(board, Move(self, t))
        return self.valid_moves

