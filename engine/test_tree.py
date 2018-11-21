import unittest
import board as b
import tree

class TreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = tree.Tree()
        self.new_board = b.Board()

    def test_check_leaves_length_1(self):
        self.tree.set_depth(1)
        self.tree.find_leaf_nodes(self.new_board, None)
        self.assertEqual(len(self.tree.leaves), 20)

    def test_check_leaves_length_2(self):
        self.tree.set_depth(2)
        self.tree.find_leaf_nodes(self.new_board, None)
        self.assertEqual(len(self.tree.leaves), 400)

    def test_moves_black_pieces_second(self):
        self.tree.set_depth(2)
        self.tree.find_leaf_nodes(self.new_board, None)
        for l in self.tree.leaves:
            print(l.move.str()+" - "+l.parent.move.str())
            self.assertFalse(l.move.piece.is_white)

    def test_only_leaves_returned(self):
        self.tree.set_depth(2)
        self.tree.find_leaf_nodes(self.new_board, None)
        for l in self.tree.leaves:
            self.assertTrue(l.parent is not None)

if __name__ == '__main__':
    unittest.main()

