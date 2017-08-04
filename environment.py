import numpy as np

class Environment:
    def __init__(self):
        self.board = np.zeros((board_length, board_length))
        self.player_one = -1 # 'x'
        self.player_two = 1 # '0'
        self.winner = None
        self.board_resolution = False
        self.board_permutations = 3**(board_length * board_length)

def get_state(self):
    '''
    Returns the current state, represented by an integer
    from 0... |S|-1, where S = set of all possible states
    |S| = 3 ^ board_size, since each cell can have 3 possible values, empty, -1, and 1.
    Some states are not possible
    Similiar to finding integer represented by base 3 number.
    '''
    # not needed?

def game_over(self, force_recalculate=False):
    if not force_recalculate and self.ended:
        return self.ended

def check_winner():
    for i in range(board_length):
        # horizontal winner?
        if abs(np.sum(board[i])) == board_length:
            print('horizontal winner!')
            self.winner = player
            self.ended = True
            return True

        # vertical winner?
        if abs(np.sum(board[:,i])) == board_length:
            print('vertical winner!')
            self.winner = player
            self.ended = True
            return True
            
        # diagonal winner? \\ top left to bottom right
        if abs(np.trace(board)) == board_length: 
            print('diagonal winner!')
            self.winner = player
            self.ended = True
            return True

        # diagonal winner? // top right to bottom left
        if abs(np.trace(np.fliplr(board))) == board_length: 
            print('diagonal winner!')
            self.winner = player
            self.ended = True
            return True
    # Is entire board filled with no winner?
    if len(moves_validate()) == 0:
        self.winner = None
        self.ended = True
        return True
    # Game is still going on!
    return False

# Finds the '0's on the board and returns their location via indices
def moves_validate():
    return np.transpose(np.where(board==0))

# returns true if position on board is valid and empty
def validate_move(self, i, j):
    return self.board[i,j]

def display_board(self):
    for i in range(board_length):
        print('----------')
        for j in range(board_length):
            print(" ")
            if self.board[i,j] == self.x:
                print("x")
            elif self.board[i,j] == self.o:
                print("o")
            else:
                print(" "),
            print("")
        print('----------')





'''
# init

# is empty

# reward

# get state

# game over

# display board
'''
