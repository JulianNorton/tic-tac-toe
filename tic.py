import random
import numpy as np

random.seed(1)

# create a square board
def clean_board():
    return np.zeros((3,3))

player_one = 1
player_two = -1

board = clean_board()
board_length = len(board)

def play_game(p1,p2,env, draw=False):
    # loop until game is over
    current_player = None
    '''
    while not env.game_over()
    alternate between players
    p1 goes first

    if current_player == player_one:
        current_player = player_two
    else:
        current_player = player_one
    
    if board_state:
        if draw

    draw board
    current_player.take_action(env)

    p1.update(env)
    p2.update(env)
    '''
    print('test')

def check_winner():
    # WINNER CHECK
    game_over = False
    for i in range(board_length):

        # horizontal winner?
        if abs(np.sum(board[i])) == board_length:
            print('horizontal winner!')
            game_over = True
            print('game over')
            quit()

        # vertical winner?
        if abs(np.sum(board[:,i])) == board_length:
            print('vertical winner!')
            game_over = True
            print('game over')
            quit()
            
        # diagonal winner? \\ top left to bottom right
        if abs(np.trace(board)) == board_length: 
            print('diagonal winner!')
            game_over = True
            print('game over')
            quit()

        # diagonal winner? // top right to bottom left
        if abs(np.trace(np.fliplr(board))) == board_length: 
            print('diagonal winner!')
            game_over = True
            print('game over')
            quit()
    return game_over

# Finds the '0's on the board and returns their location via indices
def moves_validate():
    return np.transpose(np.where(board==0))

def moves_selection(player):
    possible_moves = moves_validate()
    if len(possible_moves) > 0:
        select_move = random.choice(moves_validate())
        print(select_move)
        select_move = list(select_move)
        board[select_move[0],select_move[1]] = player
        print('(',player,')', 'making a move!')
    else:
        print('no valid moves')
        

def game_iteration():
    game_over = False
    while game_over == False:
        print(board)
        moves_selection(player_one)
        print(board)
        moves_selection(player_two)
        print(board, '\n')
        game_over = check_winner()

game_iteration()
