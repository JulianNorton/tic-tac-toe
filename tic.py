import random
import numpy as np

random.seed(1)


# create a 3x3 board
def clean_board():
    board = np.zeros((3,3))
    print(board)
# who goes first?
# first_player = random.choice(players)
player_one = 1


# board = np.ones((3,3))
board = np.zeros((3,3))

# board[0,2] = -1
# board[1,1] = -1
# board[2,0] = -1

# board[:,0] = -1
board_length = len(board)

def check_winner():
    # WINNER CHECK
    game_over = False
    for i in range(board_length):
        print(board[i,i])
        # horizontal winner?
        if abs(np.sum(board[i])) == board_length:
            print('horizontal winner!')
            game_over = True
            break

        # vertical winner?
        if abs(np.sum(board[:,i])) == board_length:
            print('vertical winner!')
            game_over = True
            break
        # diagonal winner? \\ top left to bottom right

        if abs(np.trace(board)) == board_length: 
            print('diagonal winner!')
            game_over = True
            break

        # diagonal winner? // top right to bottom left
        if abs(np.trace(np.fliplr(board))) == board_length: 
            print('diagonal winner!')
            game_over = True
            break
    return game_over

def moves_validate():
    return np.transpose(np.where(board==0))

def moves_selection(player):
    possible_moves = moves_validate()
    if len(possible_moves) > 0:
        select_move = random.choice(moves_validate())
        print(select_move)
        select_move = list(select_move)
        board[select_move[0],select_move[1]] = player
        print('making a move!')
    else:
        print('no valid moves, tie.')
        print(board)


print(moves_validate())
moves_selection(player_one)
print(board)


game_over = check_winner()

while game_over == False:
    moves_selection(player_one)
    print('game not over!!!')
    print(board)
    game_over = check_winner()
    if game_over == True:
        break



