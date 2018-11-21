import unittest
import board

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

    def test_pieces_black_and_white(self):
        black = []
        white = []
        for p in self.board.pieces:
            if p.is_white:
                white.append(p)
            else:
                black.append(p)
        self.assertEqual(len(white), 16)
        self.assertEqual(len(black), 16)

if __name__ == '__main__':
    unittest.main()

