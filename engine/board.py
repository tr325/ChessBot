import pieces as pc
import node as node
import copy

class Board():
    
    WHITE = True
    BLACK = False

    def __init__(self):
        self.pieces = []
        self._populate_new_board()
        self.to_play = self.WHITE

    def _populate_new_board(self):
        # set up a blank chess board
        self.pieces.append(pc.Rook(0,0))
        self.pieces.append(pc.Knight(1,0))
        self.pieces.append(pc.Bishop(2,0))
        self.pieces.append(pc.Queen(3,0))
        self.pieces.append(pc.King(4,0))
        self.pieces.append(pc.Bishop(5,0))
        self.pieces.append(pc.Knight(6,0))
        self.pieces.append(pc.Rook(7,0))
        for i in range(8):
            self.pieces.append(pc.Pawn(i,1))
        self.pieces.append(pc.Rook(0,7,True))
        self.pieces.append(pc.Knight(1,7,True))
        self.pieces.append(pc.Bishop(2,7,True))
        self.pieces.append(pc.Queen(3,7,True))
        self.pieces.append(pc.King(4,7,True))
        self.pieces.append(pc.Bishop(5,7,True))
        self.pieces.append(pc.Knight(6,7,True))
        self.pieces.append(pc.Rook(7,7,True))
        for i in range(8):
            self.pieces.append(pc.Pawn(i,6,True))

    # For ease of testing
    def _clear_board(self):
        self.pieces = []

    def get_piece_at(self, x, y):
        for p in self.pieces:
            if(p.is_at(x,y)):
                return p

    def remove_piece_at(self, x, y):
        p = self.get_piece_at(x, y)
        # TODO: simplest way to remove a value from an array in python?

    def change_turn(self):
        self.to_play = not self.to_play

    def render(self):
        rendered = ""
        for y in range(7,-1,-1):
            for x in range(8):
                p = self.get_piece_at(x, y)
                if(p):
                    rendered = rendered+p.str()
                else:
                    rendered = rendered+"."
            rendered = rendered+"\n"
        return rendered

if __name__ == '__main__':
    print(Board().render())

