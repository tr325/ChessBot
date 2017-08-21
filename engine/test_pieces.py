import unittest
import pieces as P

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

if __name__ == '__main__':
    unittest.main()
