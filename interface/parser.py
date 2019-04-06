
class Parser():

    # TODO: castling, enpassant, etc. where the movestr is different
    def get_move(self, user_string, board):
        string = user_string.strip()
        possible_pieces = []
        if(string[0].isupper()):
            possible_pieces = self._possible_pieces_on_board(string[0], board)
        else:
            possible_pieces = self._possible_pieces_on_board('P', board)
        return self._find_user_move(string, possible_pieces, board)

    def _possible_pieces_on_board(self, user_piece, board):
        possible_pieces = []
        for p in board.pieces:
            if(p.is_white == board.to_play):
                if(p.str().upper() == user_piece):
                    possible_pieces.append(p)
        return possible_pieces


    def _find_user_move(self, user_move_string, possible_pieces, board):
        for p in possible_pieces:
            for m in p.get_valid_moves(board):
                if(m.str() == user_move_string):
                    return m



