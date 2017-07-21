import random
import numpy as np

# create a 3x3 board
def clean_board():

    board = np.zeros((3,3))
    print(board)
# who goes first?
# first_player = random.choice(players)


board = np.zeros((3,3))
board = np.ones((3,3))
# board[0,1] = -1
board[0] = 0
board[1,1] = -1
board[2,2] = -1
board_length = len(board)


print(board)
# WINNER CHECK
for i in range(board_length):
    # horizontal winner?
    if abs(np.sum(board[i])) == board_length:
        # or -board_length
        print(np.sum(board[i]))
        print(board_length)
        print(-board_length)
        # winner = board[0, i]
        # print(board[0, i])
        # print(board, 'b', board_length, -board_length)
        # print(np.sum(board[i]))
        # print('i ==',i,'horizontal winner!', winner)
        break
    # Horizontal winner?
    # if np.sum([board[i]], axis=1) == board_length or -board_length:
    #     winner = board[0, i]
    #     print(board[0, i])
    #     print(board)
    #     print(np.sum(board[i]))
    #     print('vertical winner!', winner)
    #     break
    else:
        print(board)
    # if np.sum(board[i]) == 3 or -3:
    #     winner = board[0, i]
    #     print('winner!', winner)
    #     break


