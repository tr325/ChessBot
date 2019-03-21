
class Parser():

    # TODO: castling, enpassant, etc. where the movestr is different
    def get_move(self, string, board):
        s = string.split(' ')
        sx = string.split('x')
        possible_pieces = []
        if(len(s) == 2):
            possible_pieces = self._possible_pieces_on_board(s[0], board)
        elif(len(sx) == 2):
            possible_pieces =  self._possible_pieces_on_board(sx[0], board)
        else:
            possible_pieces = self._possible_pieces_on_board('P', board)
        return self._find_user_move(string, possible_pieces, board)

    def _possible_pieces_on_board(self, user_string_parts, board):
        # Maybe....
        # ... find pieces of right kind from board (new argument to init?) and check if any of their valid_moves is the same as that constructed here by user input?
            # 1. for all pieces, p.str() == user_string_parts[0]
            # 2. for all pices of the right kind:
            # 3. do any of that piece's valid moves have the same move
            #       string as entered by the user
        possible_pieces = []
        for p in board.pieces:
            if(p.is_white == board.to_play):
                if(p.str().upper() == user_string_parts[0]):
                    possible_pieces.append(p)
        return possible_pieces


    def _find_user_move(self, user_move_string, possible_pieces, board):
        for p in possible_pieces:
            for m in p.get_valid_moves(board):
                if(m.str() == user_move_string):
                    return m



