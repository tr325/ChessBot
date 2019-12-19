import readline
import engine.board as Board
import engine.tree as Tree
import interface.parser as Parser
import decision.naive as Naive

board = Board.Board()
tree = Tree.Tree()
tree.set_depth(2)
parser = Parser.Parser()
naive = Naive.Naive()
while(True):
    print(board.render())
    
    # User move (plays white)
    user_input = str(input("Play a move: "))
    move = parser.get_move(user_input, board)
    while(move is None):
        user_input = str(input("Sorry, that's not a valid move - try again: "))
        move = parser.get_move(user_input, board)
    move.apply(board)
    print(board.render())

    # Engine move (plays black)
    computer_move = naive.get_best_move(board)
    computer_move.apply(board)
