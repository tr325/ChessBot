import unittest
import interface.parser as parser
import engine.board as board
import engine.pieces as pieces

class ParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = parser.Parser()
        self.board = board.Board()

    def assertMoveValid(self, user_move):
        move = self.parser.get_move(user_move, self.board)
        self.assertEqual(move.str(), user_move)

    def assertMoveInvalid(self, user_move):
        move = self.parser.get_move(user_move, self.board)
        self.assertEqual(move, None)

    def test_piece_move(self):
        self.assertMoveValid('N c3')

    def test_invalid_move_destination(self):
        self.assertMoveInvalid('N c4')

    def test_wrong_colour_moved(self):
        self.assertMoveInvalid('N c6')

    def test_pawn_move(self):
        self.assertMoveValid('d4')

    def test_capture(self):
        bishop = pieces.Bishop(7,5) # h6
        self.board.pieces.append(bishop)
        self.assertMoveValid('Bxg7')

    def test_pawn_capture(self):
        self.board._setup_position_from_representation((
            "rnbqkbnr\n"
            "pp..pppp\n"
            "........\n"
            "..pp....\n"
            "..PP....\n"
            "........\n"
            "PP..PPPP\n"
            "RNBQKBNR"))
        self.assertMoveValid('xc5')

