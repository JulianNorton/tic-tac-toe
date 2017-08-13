import random
import numpy as np
import copy

random.seed(0)

verbose = True

# Agent, Environment, State, Action, Reward, Episodes, Terminal State

# -------------------------------
# ENVIRONMENT defines the rules of the game
# -------------------------------
class Environment():
    # todo, make board length separate from win condition k ('in a row')
    def __init__(self, board_length):
        self.winner = None
        self.game_over = False
        self.board_length = board_length
        empty_board = np.zeros((board_length, board_length))
        self.board_state = empty_board
        self.board_items_maximum = board_length*board_length

    def reward(self):
        if self.game_over == True:
            return 1
        else:
            return -1


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
            elif abs(np.sum(self.board_state[:,i])) == self.board_length:
                self.winner = True
                self.game_over = True
                if verbose == True : print('\n', 'vertical win', self.game_over)
                return True
                
            # diagonal winner? \\ top left to bottom right
            elif abs(np.trace(self.board_state)) == self.board_length: 
                self.winner = True
                self.game_over = True
                if verbose == True : print('\n', 'diagonal win \\ ', self.game_over)
                return True

            # diagonal winner? // top right to bottom left
            elif abs(np.trace(np.fliplr(self.board_state))) == self.board_length: 
                self.winner = True
                self.game_over = True
                if verbose == True : print('\n', 'diagonal win //', self.game_over)
                return True

            # Check if there's a tie
            elif np.count_nonzero(self.board_state) == self.board_items_maximum:
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
        # TODO, make state history matter.
        self.state_history = [] 
        # player value, -1 or 1. 
        self.player = player

    def reset_history(self):
        self.state_history = []

    # Evaluate moves to determine best move for next action
    def evaluate_move(self, env):
        # TODO, don't repeat legal moves
        legal_moves = np.transpose(np.where(env.board_state==0))
        # copies current state to explore actions
        future_state = copy.deepcopy(env)
        # Loops through all legal moves
        for i in legal_moves:
            # i returns a coordinate like [0 2]
            future_state.board_state[i[0], i[1]] = self.player
            # Reward returns a negative value if no win condition met
            # Positive reward if there is a win condition
            if future_state.episode_resolution() == True:
                current_move = i
                # end loop if a good move has been found
                return current_move
            else:
                future_state.board_state[i[0], i[1]] = 0
        # If no best move found, return a random move
        current_move = random.choice(legal_moves)
        return current_move
            
    def take_action(self, env):
        try:
            current_move = self.evaluate_move(env)
            env.board_state[current_move[0],current_move[1]] = self.player
        except:
            if verbose == True : print('no available moves')
            quit()


# -------------------------------

env = Environment(3)
player_ann = Agent(-1)
player_bob = Agent(1)


def game_iteration(iterations):
    for i in range(iterations):
        while env.game_over == False:
            player_ann.take_action(env)
            if env.episode_resolution() == True:
                if verbose == True : print('\n', 'Game!', env.episode_resolution(), '\n')
                break
            player_bob.take_action(env)
            if env.episode_resolution() == True:
                if verbose == True : print('\n', 'Game!', env.episode_resolution(), '\n')
            if verbose == True : print(env.board_state, '\n', 'Current state', env.episode_resolution(), '\n')
    print(env.board_state)

game_iteration(1)
