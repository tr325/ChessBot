import unittest
import board as b
import tree

class TreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = tree.Tree()

    def test_check_leaves_length_1(self):
        self.tree.set_depth(1)
        self.tree.find_leaf_nodes(None)
        for l in self.tree.leaves:
            print(l.move.str())
        self.assertEqual(len(self.tree.leaves), 20)

    def test_check_leaves_length_2(self):
        self.tree.set_depth(2)
        self.tree.find_leaf_nodes(None)
        self.assertEqual(len(self.tree.leaves), 400)

if __name__ == '__main__':
    unittest.main()

