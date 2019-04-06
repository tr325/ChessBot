import readline
import engine.board as Board
import interface.parser as Parser


board = Board.Board()
parser = Parser.Parser()
while(True):
    print(board.render())
    
    user_input = str(input("Play a move: "))
    move = parser.get_move(user_input, board)
    while(move is None):
        user_input = str(input("Sorry, that's not a valid move - try again: "))
        move = parser.get_move(user_input, board)
    move.apply(board)

