
class Piece():
    display_as = "x" # Overwrite in child classes
    
    # More natural to create pieces with blank constructor for white,
    # Code is more natural checking for "whiteness" first
    def __init__(self, is_black=False):
        self.is_white = not is_black
        
    def str(self):
        if(self.is_white):
            return self.display_as.upper()
        else:
            return self.display_as


#####################
class Pawn(Piece):
    display_as = "p"

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
