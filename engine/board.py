import pieces as pc
import node as node

class Board():
    
    # Number of moves calculated
    MAX_DEPTH = 1

    WHITE = True
    BLACK = False

    def __init__(self):
        self.pieces = []
        self._populate_new_board()
        self.node_tree = [[]]
        self.to_play = self.WHITE

    # For ease of testing
    def _clear_board(self):
        self.pieces = []

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

    def get_piece_at(self, x, y):
        for p in self.pieces:
            if(p.is_at(x,y)):
                return p

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

    def populate_node_tree(self):
        for i in range(self.MAX_DEPTH):
            for p in self.pieces:
                if(p.is_white == self.to_play):
                    # TODO: Pass in copy of board when self.MAX_DEPTH > 1
                    for m in p.get_valid_moves(self):
                        # TODO: Track parent node when self.MAX_DEPTH > 1
                        n = node.Node(None, m)
                        self.node_tree[i].append(n)

if __name__ == '__main__':
    print(Board().render())

