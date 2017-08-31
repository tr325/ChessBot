import unittest
import move
import board
import pieces as pc
from transform import Transform as T

class MoveTest(unittest.TestCase):

    def setUp(self):
        self.board = board.Board()

    def test_is_valid_board_limits(self):
        q = pc.Queen(0,0)
        self.assertTrue(move.Move(self.board, q, T(1,1,1)).is_valid())
        self.assertFalse(move.Move(self.board, q, T(-1,1,1)).is_valid())
        self.assertFalse(move.Move(self.board, q, T(1,-1,1)).is_valid())
        n = pc.Knight(6,6)
        self.assertTrue(move.Move(self.board, n, T(-2,1,1)).is_valid())
        self.assertFalse(move.Move(self.board, n, T(2,1,1)).is_valid())
        self.assertFalse(move.Move(self.board, n, T(-1,2,1)).is_valid())

    def test_is_valid_obstructed(self):
        q = pc.Queen(3,3)
        p = pc.Pawn(3,4)
        b = board.Board()
        b.pieces.extend([q,p])
        self.assertTrue(move.Move(b, q,  T(1,1,1)).is_valid())
        self.assertFalse(move.Move(b, q, T(0,1,2)).is_valid())

    def test_is_valid_capture(self):
        q = pc.Queen(3,3)
        p = pc.Pawn(3,4)
        r = pc.Rook(2,3,True)
        b = board.Board()
        b.pieces.extend([q,p,r])
        print(1)
        #self.assertTrue(move.Move(b, q,  T(1,1,1)).is_valid())
        print(2)
        print("LALAL", move.Move(b, q, T(0,1,1)).is_valid())
        self.assertFalse(move.Move(b, q, T(0,1,1)).is_valid())
        print(3)
        print(q.x)
        print(q.y)
        #self.assertTrue(move.Move(b, q, T(-1,0,1)).is_valid())

    def test_apply(self):
        b = pc.Bishop(5,5)
        m = move.Move(self.board, b, T(-1,-1,3))
        m.is_valid()
        m.apply()
        self.assertEqual(b.get_position()[0], 2)
        self.assertEqual(b.get_position()[1], 2)

if __name__ == '__main__':
    unittest.main()

