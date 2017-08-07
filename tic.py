import random
import numpy as np

random.seed(0)

verbose = True

# Agent, Environment, State, Action, Reward, Episodes, Terminal State

# -------------------------------
# ENVIRONMENT defines the rules of the game
# -------------------------------
class Environment():
    def __init__(self, board_length):
        self.winner = None
        self.game_over = False
        self.board_length = board_length
        empty_board = np.zeros((board_length, board_length))
        self.board_state = empty_board
        self.board_items_maximum = board_length*board_length
        # self.board_state[0] = 0

    # Checking to see if there's a tie or anyone has won the game
    def episode_resolution(self):
        for i in range(self.board_length):
            # horizontal winner?
            if abs(np.sum(self.board_state[i])) == self.board_length:
                self.winner = True
                self.game_over = True
                if verbose == True : print('\n', 'horizontal win', self.game_over)
                return True

            # vertical winner?
            if abs(np.sum(self.board_state[:,i])) == self.board_length:
                self.winner = True
                self.game_over = True
                if verbose == True : print('\n', 'vertical win', self.game_over)
                return True
                
            # diagonal winner? \\ top left to bottom right
            if abs(np.trace(self.board_state)) == self.board_length: 
                self.winner = True
                self.game_over = True
                if verbose == True : print('\n', 'diagonal win \\ ', self.game_over)
                return True

            # diagonal winner? // top right to bottom left
            if abs(np.trace(np.fliplr(self.board_state))) == self.board_length: 
                self.winner = True
                self.game_over = True
                if verbose == True : print('\n', 'diagonal win //', self.game_over)
                return True

            # Check if there's a tie
            if np.count_nonzero(self.board_state) == self.board_items_maximum:
                self.winner = False
                self.game_over = True
                if verbose == True : print('\n', 'tied game', self.game_over)
                return True

# -------------------------------
# AGENT plays the game
# -------------------------------
class Agent:
    def __init__(self, player, eps=0.1, alpha=0.5):
        self.eps = eps # probability of choosing random action instead of greedy
        self.alpha = alpha # learning rate
        self.state_history = []
        self.player = player

    def reset_history(self):
        self.state_history = []

    def take_action(self, env):
        # Finds the '0's on the board and returns their location via indices
        try:
            available_moves = np.transpose(np.where(env.board_state==0))
            if verbose == True : print('available moves\n', available_moves, '\n')
            select_move = random.choice(available_moves)
            if verbose == True : print('player=', self.player,'selected move',select_move)
            env.board_state[select_move[0], select_move[1]] = self.player
        except:
            if verbose == True : print('no available moves')
            quit()


# -------------------------------

env = Environment(3)
player_one = Agent(-1)
player_two = Agent(1)

def game_iteration(iterations):
    for i in range(iterations):
        while env.game_over == False:
            player_one.take_action(env)
            if verbose == True : print('\n', 'Game over?', env.episode_resolution(), '\n')
            env.episode_resolution
            player_two.take_action(env)
            if verbose == True : print('\n', 'Game over?', env.episode_resolution(), '\n', env.board_state)

game_iteration(2)