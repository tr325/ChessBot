import unittest
import board as b
import tree

#TODO: use assertIsNone, assertIsNotNone
class TreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = tree.Tree()
        self.new_board = b.Board()

    def test_check_leaves_length_1(self):
        b = self.new_board
        self.tree.set_depth(1)
        self.tree.find_leaf_nodes(b, None)
        self.assertEqual(len(self.tree.leaves), 20)
        self.assertEqual(len(b.pieces), 32)

    def test_check_leaves_length_2(self):
        self.tree.set_depth(2)
        self.tree.find_leaf_nodes(self.new_board, None)
        self.assertEqual(len(self.tree.leaves), 400)

    def test_moves_black_pieces_second(self):
        self.tree.set_depth(2)
        self.tree.find_leaf_nodes(self.new_board, None)
        for l in self.tree.leaves:
            self.assertFalse(l.move.piece.is_white)

    def stringify(self, leaf):
        return leaf.parent.move.str()+" - "+leaf.move.str() 

    # TEMP test to check if there are the right numbers of *unique* moves
    # ... then find out why there are duplicates later
    def test_TEMP_unique_leaves_length_2(self):
        self.tree.set_depth(2)
        self.tree.find_leaf_nodes(self.new_board, None)
        leaf_strings = []
        for l in self.tree.leaves:
            s = self.stringify(l)
            if not s in leaf_strings:
                leaf_strings.append(s)
        self.assertEqual(len(leaf_strings), 400)

    def test_only_leaves_returned(self):
        self.tree.set_depth(2)
        self.tree.find_leaf_nodes(self.new_board, None)
        for l in self.tree.leaves:
            self.assertTrue(l.parent is not None)

if __name__ == '__main__':
    unittest.main()

