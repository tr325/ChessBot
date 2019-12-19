import unittest
import engine.move as move
import engine.board as board
import engine.pieces as pc
from engine.transform import Transform as T

class MoveTest(unittest.TestCase):

    def test_is_valid_board_limits(self):
        q = pc.Queen(0,0)
        b = board.Board()
        # Remove initial board setup
        b.pieces = [q]
        self.assertTrue(move.Move(q, T(1,1,1)).is_valid(b))
        self.assertFalse(move.Move(q, T(-1,1,1)).is_valid(b))
        self.assertFalse(move.Move(q, T(1,-1,1)).is_valid(b))
        n = pc.Knight(6,6)
        self.assertTrue(move.Move(n, T(-2,1,1)).is_valid(b))
        self.assertFalse(move.Move(n, T(2,1,1)).is_valid(b))
        self.assertFalse(move.Move(n, T(-1,2,1)).is_valid(b))

    def test_is_valid_obstructed(self):
        q = pc.Queen(3,3)
        p = pc.Pawn(3,4)
        b = board.Board()
        b.pieces.extend([q,p])
        self.assertTrue(move.Move(q,  T(1,1,1)).is_valid(b))
        self.assertFalse(move.Move(q, T(0,1,2)).is_valid(b))
        self.assertFalse(move.Move(q, T(0,1,1)).is_valid(b))

    def test_is_valid_capture(self):
        q = pc.Queen(3,3)
        p = pc.Pawn(3,4)
        r = pc.Rook(2,3,True)
        b = board.Board()
        b.pieces.extend([q,p,r])
        self.assertTrue(move.Move(q, T(1,1,1)).is_valid(b))
        self.assertFalse(move.Move(q, T(0,1,1)).is_valid(b))
        self.assertTrue(move.Move(q, T(-1,0,1)).is_valid(b))

    def test_capture_value(self):
        q = pc.Queen(3,3)
        p = pc.Pawn(3,4)
        r = pc.Rook(2,3,True)
        b = board.Board()
        b.pieces.extend([q,p,r])
        m1 = move.Move(q, T(1,1,1))
        self.assertTrue(m1.is_valid(b))
        self.assertEqual(m1.value(b), 0)
        self.assertFalse(move.Move(q, T(0,1,1)).is_valid(b))
        m2 = move.Move(q, T(-1,0,1))
        self.assertTrue(m2.is_valid(b))
        self.assertEqual(m2.value(b), 5)

    def test_apply(self):
        b = pc.Bishop(5,5)
        m = move.Move(b, T(-1,-1,3))
        bo = board.Board()
        self.assertTrue(bo.to_play == bo.WHITE)
        m.is_valid(bo)
        m.apply(bo)
        self.assertTrue(bo.to_play == bo.BLACK)
        self.assertEqual(b.get_position()[0], 2)
        self.assertEqual(b.get_position()[1], 2)
        self.assertTrue(bo.get_piece_at(5,5) is None)

    def test_undo(self):
        b = pc.Bishop(5,5)
        q = pc.Queen(6,6,True)
        bo = board.Board()
        bo._clear_board()
        bo.pieces.append(b)
        bo.pieces.append(q)
        m = move.Move(b, T(1,1,1))
        m.is_valid(bo)
        self.assertTrue(bo.to_play == bo.WHITE)
        m.apply(bo)
        m.undo(bo)
        self.assertTrue(bo.to_play == bo.WHITE)
        self.assertEqual(b.get_position()[0], 5)
        self.assertEqual(b.get_position()[1], 5)
        self.assertEqual(bo.get_piece_at(6,6), q)

    def test_negative_magnitude(self):
        p = pc.Pawn(5,5, True)
        bo = board.Board()
        bo._clear_board()
        bo.pieces.append(p)
        m = move.Move(p, T(0,-1,1))
        m.is_valid(bo)
        m.apply(bo)
        self.assertEqual(p.get_position()[0], 5)
        self.assertEqual(p.get_position()[1], 4)

if __name__ == '__main__':
    unittest.main()

