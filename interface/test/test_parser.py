import unittest
import interface.parser as parser
import engine.board as board
import engine.pieces as pieces

class ParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = parser.Parser()
        self.board = board.Board()

    def test_piece_move(self):
        user_move = 'N c3'
        move = self.parser.get_move(user_move, self.board)
        self.assertEqual(move.str(), user_move)

    def test_invalid_move_destination(self):
        user_move = 'N c4'
        move = self.parser.get_move(user_move, self.board)
        self.assertEqual(move, None)

    def test_wrong_colour_moved(self):
        user_move = 'N c6'
        move = self.parser.get_move(user_move, self.board)
        self.assertEqual(move, None)

    def test_pawn_move(self):
        user_move = 'd4'
        move = self.parser.get_move(user_move, self.board)
        self.assertEqual(user_move, move.str())

    def test_capture(self):
        bishop = pieces.Bishop(7,5) # h6
        self.board.pieces.append(bishop)
        user_move = 'Bxg7'
        move = self.parser.get_move(user_move, self.board)
        self.assertEqual(user_move, move.str())

