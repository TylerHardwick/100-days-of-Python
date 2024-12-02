from board import Board


bd = Board()

print("XOXO Welcome to Tyler's TicTacToe XOXO\n\n")
bd.chose_player()

while bd.play:
    bd.take_turn()

print("Thanks for playing Tyler's TicTacToe!")