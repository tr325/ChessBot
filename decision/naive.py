import engine.tree as t

class Naive():

    def get_best_move(self, board):
        tree = t.Tree()
        tree.set_depth(2)
        tree.find_leaf_nodes(board, None)
        current_best = 0
        best_move = None
        # for each leaf, score all nodes on branch until parent is none
        for leaf in tree.leaves:
            current_node = leaf
            if(current_node.player == board.to_play):
                score = current_node.value
            else:
                score = -current_node.value
            # TODO: Current looks for best max score. Change to
            # look instead for best MIN score (ie, no loss of material)
            while current_node.parent is not None:
                current_node = current_node.parent
                if(current_node.player == board.to_play):
                    score = score+current_node.value
                else:
                    score = score-current_node.value
            if(score >= current_best):
                current_best = score
                # current_node is now the root
                best_move = current_node.move
        return best_move
