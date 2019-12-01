import engine.tree as t

class Naive():

    def get_best_move(self, board):
        tree = t.Tree()
        tree.set_depth(2)
        tree.find_leaf_nodes(board, None)
        current_best = 0
        best_move = None
        # for each leaf, score branch until.. parent is none
        for leaf in tree.leaves:
            score = 0
            current_leaf = leaf
            while current_leaf.parent is not None:
                score = score+current_leaf.value
                current_leaf = current_leaf.parent
            score = score+current_leaf.value
            # compare score to currentBest.
            if(score >= current_best):
                best_move = current_leaf.move
        return best_move
