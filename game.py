def print_board(board):
  print("{} | {} | {}\n{} | {} | {}\n{} | {} | {}".format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]))

def start_game(p1):
  board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  print_board(board)

def new_game():
    piece = input('Player 1, would you like to be X or O? ')
    if piece not in ['X','O']:
        new_game()
    start_game(piece)
new_game()
