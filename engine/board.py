import pieces as pc

class Board():
    
    def __init__(self):
        self.board = [[None for i in range(8)] for i in range(8)]
        # set up a blank chess board
        self.board[0][0] = pc.Rook()
        self.board[0][1] = pc.Knight()
        self.board[0][2] = pc.Bishop()
        self.board[0][3] = pc.King()
        self.board[0][4] = pc.Queen()
        self.board[0][5] = pc.Bishop()
        self.board[0][6] = pc.Knight()
        self.board[0][7] = pc.Rook()
        self.board[1] = [pc.Pawn() for i in range(8)]
        self.board[7][0] = pc.Rook(True)
        self.board[7][1] = pc.Knight(True)
        self.board[7][2] = pc.Bishop(True)
        self.board[7][3] = pc.King(True)
        self.board[7][4] = pc.Queen(True)
        self.board[7][5] = pc.Bishop(True)
        self.board[7][6] = pc.Knight(True)
        self.board[7][7] = pc.Rook(True)
        self.board[6] = [pc.Pawn(True) for i in range(8)]

    def render(self):
        rendered = ""
        for i in range(7,-1,-1):
            for j in range(7,-1,-1):
                if self.board[i][j]:
                    rendered = rendered+self.board[i][j].str()
                else:
                    rendered = rendered+"."
            rendered = rendered+"\n"
        return rendered

if __name__ == '__main__':
    print(Board().render())