import engine.board as Board


board = Board.Board()
while(True):
    print(board.render())
    
    move = input("Play a move: ")

