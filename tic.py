import random
import numpy as np

# create a 3x3 board
def clean_board():
    board = np.zeros((3,3))
    print(board)
# who goes first?
# first_player = random.choice(players)


# board = np.ones((3,3))
board = np.zeros((3,3))

board[0,2] = -1
board[1,1] = -1
board[2,0] = -1

# board[:,0] = -1
board_length = len(board)

def check_winner():
    # WINNER CHECK
    for i in range(board_length):
        print(board[i,i])
        # horizontal winner?
        if abs(np.sum(board[i])) == board_length:
            print('horizontal winner!')
            break
        # vertical winner?
        if abs(np.sum(board[:,i])) == board_length:
            print('vertical winner!')
            break
        # diagonal winner? \\ top left to bottom right
        if abs(np.trace(board)) == board_length: 
            print('diagonal winner!')
            break
        # diagonal winner? // top right to bottom left

        if abs(np.trace(np.fliplr(board))) == board_length: 
            print('diagonal winner!')
            break
def valid_moves():
    return np.transpose(np.where(board==0))

check_winner()


print(valid_moves())
print(board)


