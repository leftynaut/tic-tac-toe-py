def print_board(board):
  print(" {} | {} | {}\n-----------\n {} | {} | {}\n-----------\n {} | {} | {}".format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]))

def check_win(player, board):
  if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]:
    print("{} is the winner".format(player))

def new_turn(player, board):
  move = int(input("{}, what square would you like to play? ".format(player)))
  if board[move - 1] in ['X', 'O']:
    print("That square has already been played")
    new_turn(player, board)
  board[move - 1] = player
  print_board(board)
  check_win(player, board)
  if player == 'X':
    player = 'O'
  else:
    player = 'X'
  new_turn(player, board)

def start_game(p1):
  board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  print_board(board)
  new_turn(p1, board)

def new_game():
    piece = input("Player 1, would you like to be X or O? ")
    if piece not in ['X','O']:
        new_game()
    start_game(piece)
new_game()
