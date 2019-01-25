import unittest
import board as b
import tree

#TODO: use assertIsNone, assertIsNotNone
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
        b = self.new_board
        self.tree.set_depth(1)
        self.tree.find_leaf_nodes(b, None)
        self.assertEqual(len(self.tree.leaves), 20)
        self.assertEqual(len(b.pieces), 32)

    # Check there are the right number of black first moves
    def test_TEMP_check_black_leaves_length_1(self):
        b = self.new_board
        self.tree.set_depth(1)
        b.change_turn()
        self.tree.find_leaf_nodes(b, None)
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

    #---------------------------------------------
    # Below here: only tests to track down length two move count issue
    # TODO: review which are needed when that's resolved

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

    def test_length_each_branch(self):
        self.tree.set_depth(2)
        self.tree.find_leaf_nodes(self.new_board, None)
        branches = {}
        for l in self.tree.leaves:
            parent = l.parent.move.str()
            if(not parent in branches):
                branches[parent] = []
            branches[parent].append(l.move.str())
        for b in branches:
            print(len(branches[b]))


if __name__ == '__main__':
    unittest.main()

