import unittest
import pieces as P
import board as B

class PiecesTest(unittest.TestCase):

    def test_rendering(self):
        R = P.Rook(0,0)
        r = P.Rook(7,7,True)
        self.assertEqual(r.str(), "r")
        self.assertEqual(R.str(), "R")

    def test_is_at(self):
        n = P.Knight(1,2)
        self.assertTrue(n.is_at(1,2))
        self.assertFalse(n.is_at(4,4))

    def test_get_position(self):
        q = P.Queen(4,5)
        pos = q.get_position()
        self.assertEqual(pos[0], 4)
        self.assertEqual(pos[1], 5)

    # ----------------------------------------------
    # Tests for initial number of moves

    def initial_move_counts(self, piece, board):
        if piece.str().lower() == 'p':
            self.assertEqual(len(piece.get_valid_moves(board)), 2)
            return
        if piece.str().lower() == 'r':
            self.assertEqual(len(piece.get_valid_moves(board)), 0)
            return
        if piece.str().lower() == 'n':
            self.assertEqual(len(piece.get_valid_moves(board)), 2)
            return
        if piece.str().lower() == 'b':
            self.assertEqual(len(piece.get_valid_moves(board)), 0)
            return
        if piece.str().lower() == 'q':
            self.assertEqual(len(piece.get_valid_moves(board)), 0)
            return
        if piece.str().lower() == 'k':
            self.assertEqual(len(piece.get_valid_moves(board)), 0)
            return
        # Sanity check - should never reach here
        self.assertTrue(False)

    def test_new_board_move_counts(self):
        board = B.Board()
        for p in board.pieces:
            self.initial_move_counts(p, board)

if __name__ == '__main__':
    unittest.main()
