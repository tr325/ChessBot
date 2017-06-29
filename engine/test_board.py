import unittest
import board

class BoardTest(unittest.TestCase):
    
    def setUp(self):
        self.board = board.Board()
        
    def test_board_size(self):
        self.assertEqual(self.board.board[0][0].str(), "R")
        self.assertEqual(self.board.board[7][7].str(), "r")
        with self.assertRaises(IndexError):
            self.board.board[9][9]

    def test_blank_render(self):
        self.assertEqual(self.board.render(),
            "rnbkqbnr\n"+
            "pppppppp\n"+
            "........\n"+
            "........\n"+
            "........\n"+
            "........\n"+
            "PPPPPPPP\n"+
            "RNBKQBNR\n")


if __name__ == '__main__':
    unittest.main()