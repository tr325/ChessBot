import node as N
import board as B

class Tree():
    
    def __init__(self):
        self.leaves = []

    def set_depth(self, depth):
        self.max_depth = depth

    # TODO: Rather than populate a tree of boards, evalute the score of each branch and store that
    # 'scoring' scheme gives decision, eg. "max points gained at leaf"
    # Do a depth-first search of the tree, allowing boards for nodes to go out of scope when you've
    # evaluated the branch score.
    #
    # TODO: Initial (inefficient) version could just re-evaluate each branch from depth 1 -> N rather
    # than store the board on the node?
    def find_leaf_nodes(self, board, parent_node):
        for p in board.pieces:
            if(p.is_white == board.to_play):
                for m in p.get_valid_moves(board):
                    m.apply(board)
                    n = N.Node(parent_node, board, m)
                    if(n.depth == self.max_depth):
                        self.leaves.append(n)
                    else:
                        self.find_leaf_nodes(board, n)
                    m.undo(board)

    # TODO: Doesn't live here
    #def evaluate_branch(self, leaf_node):
        # Use node.parent recursively to find point score for branch


