
class Parser():

    # TODO: castling, enpassant, etc. where the movestr is different
    def get_move(self, string):
        s = string.split('')
        sx = string.split('x')
        if(len(s) == 2):
            return _get_move_default(s)
        elif(len(sx) == 2):
            return _get_move_default(s, True)
        else:
            # pawn move - parse a little differently
            return


