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

    def test_takes_free_piece(self):
        board = self.new_board
        board._setup_position_from_representation(
            "rnbqkbnr\n"
            "p.pppppp\n"
            "........\n"
            ".p......\n"
            "..P.....\n"
            "........\n"
            "PP.PPPPP\n"
            "RNBQKBNR\n")
        board.get_piece_at(1,4).has_moved = True
        board.get_piece_at(2,3).has_moved = True
        board.to_play = self.new_board.WHITE
        move = self.naive.get_best_move(board)
        self.assertEqual(move.str(), "xb5")
        self.assertEqual(move.value(board), 1)

    def test_takes_correct_free_piece(self):
        board = self.new_board
        board._setup_position_from_representation(
            "rnbqkbnr\n"
            "p.pppppp\n"
            "........\n"
            ".p.b....\n"
            "..B.....\n"
            "........\n"
            "PP.PPPPP\n"
            "RNBQKBNR\n")
        board.get_piece_at(1,4).has_moved = True
        board.get_piece_at(2,3).has_moved = True
        board.get_piece_at(3,4).has_moved = True
        board.to_play = self.new_board.WHITE
        move = self.naive.get_best_move(board)
        self.assertEqual(move.str(), "Bxd5")
        self.assertEqual(move.value(board), 3)
