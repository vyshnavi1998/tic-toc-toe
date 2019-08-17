#global_variavles


#board
board=["-","-","-",
       "-","-","-",
       "-","-","-",]

winner=None

#who's turn 
current_player="X"


game_still_going=True


#display
def display_board():
  print(board[0]+" | "+board[1]+" | "+board[2])
  print(board[3]+" | "+board[4]+" | "+board[5])
  print(board[6]+" | "+board[7]+" | "+board[8])


def play_game():
 #dispay board
  display_board()
  #while the game is still going
  while game_still_going:
  
    #handle single turn of player
    handle_turn(current_player)


    #checks game is over or not
    check_if_game_over()
    
    #flip to other player
    flip_player()

  #print winner
  if winner=="X" or winner=="O":
    print(winner+" won!")
  #if the game is tie
  else:
    print("tie!")

#handle a single turn
def handle_turn(player):

  print(player+"'s turn")
  position=input("choose from 1 to 9 : ")
  valid=False
  while not valid:
    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position=input("choose from 1 to 9 : ")
    position=int(position)-1
    if board[position]=="-":
      valid=True
    else:
      print("you cant go there")
  board[position]=player
  display_board()


def check_if_game_over():
  check_win()
  check_tie()


def check_win():
  global winner
  #check rows
  row_winner=check_rows()
  #check colums
  col_winner=check_cols()
  
  #check diagonals
  diag_winner=check_diag()

  if row_winner:
    #there was a win
    winner=row_winner
  elif col_winner:
    #there was a win
    winner=col_winner

  elif diag_winner:
    #there was a win
    winner=diag_winner

  else:
    winner=None
    #there was no win

  return


def check_rows():
  global game_still_going

  row_1=board[0]==board[1]==board[2]!="-"
  row_2=board[3]==board[4]==board[5]!="-"
  row_3=board[6]==board[7]==board[8]!="-"

  if row_1 or row_2 or row_3:
    game_still_going=False
  #return the winner
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]

  return

def check_cols():
  global game_still_going

  col_1=board[0]==board[3]==board[6]!="-"
  col_2=board[1]==board[4]==board[7]!="-"
  col_3=board[2]==board[5]==board[8]!="-"

  if col_1 or col_2 or col_3:
    game_still_going=False
  #return the winner
  if col_1:
    return board[0]
  elif col_2:
    return board[1]
  elif col_3:
    return board[2]

  return


def check_diag():
  global game_still_going

  dag_1=board[0]==board[4]==board[8]!="-"
  dag_2=board[2]==board[4]==board[6]!="-"

  if dag_1 or dag_2:
    game_still_going=False
  #return the winner
  if dag_1:
    return board[0]
  elif dag_2:
    return board[2 ]
  return



def check_tie():
  global game_still_going
  if "-" not in board:
    game_still_going=False
  return


def flip_player():
  global current_player
  if current_player=="X":
    current_player="O"
  elif current_player=="O":
    current_player="X"
  return


play_game()
#play game
#handle turn
# check win
  
#check tie
#flip player
