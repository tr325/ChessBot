import unittest
import engine.board as b
import engine.tree as tree

class TreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = tree.Tree()
        self.new_board = b.Board()

    # Utilities
    def stringify(self, leaf):
        return leaf.parent.move.str()+" - "+leaf.move.str()

    #--------------------------------------------------
    # Tests

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
            self.assertFalse(l.move.piece.is_white)

if __name__ == '__main__':
    unittest.main()

