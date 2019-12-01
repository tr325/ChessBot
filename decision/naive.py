import engine.tree as t

class Naive():

    def get_best_move(self, board):
        tree = t.Tree()
        tree.set_depth(2)
        tree.find_leaf_nodes(board, None)
        return tree.leaves[0].parent.move
