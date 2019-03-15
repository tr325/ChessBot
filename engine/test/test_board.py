import unittest
import engine.board as board

class BoardTest(unittest.TestCase):
    
    def setUp(self):
        self.board = board.Board()

    def test_get_piece_at(self):
        b = self.board
        self.assertEqual(b.get_piece_at(0,0).str(), "R")
        self.assertEqual(b.get_piece_at(3,0).str(), "Q")
        self.assertEqual(b.get_piece_at(5,5), None)
        self.assertEqual(b.get_piece_at(7,6).str(), "p")

    def test_pieces_length(self):
        self.assertEqual(len(self.board.pieces), 32)

    def test_blank_render(self):
        self.assertEqual(self.board.render(),
            "rnbqkbnr\n"+
            "pppppppp\n"+
            "........\n"+
            "........\n"+
            "........\n"+
            "........\n"+
            "PPPPPPPP\n"+
            "RNBQKBNR\n")

    def test_remove_piece_at(self):
        b = self.board
        b.remove_piece_at(0,0)
        b.remove_piece_at(6,6)
        self.assertEqual(self.board.render(),
            "rnbqkbnr\n"+
            "pppppp.p\n"+
            "........\n"+
            "........\n"+
            "........\n"+
            "........\n"+
            "PPPPPPPP\n"+
            ".NBQKBNR\n")

if __name__ == '__main__':
    unittest.main()

