import unittest
import engine.board as b
import decision.naive as n

class NaiveTest(unittest.TestCase):

    def setUp(self):
        self.new_board = b.Board()
        self.naive = n.Naive()

    def test_returns_correct_colour_move(self):
        move = self.naive.get_best_move(self.new_board)
        self.assertEqual(move.piece.is_white, self.new_board.to_play)

