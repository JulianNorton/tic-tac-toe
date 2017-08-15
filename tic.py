import random
import numpy as np
import copy

# Agent, Environment, State, Action, Reward, Episodes, Terminal State

# -------------------------------
# ENVIRONMENT defines the rules of the game
# -------------------------------
class Environment():
    def __init__(self, board_length, win_condition):
        self.winner = None
        self.game_over = False
        self.board_length = board_length
        # Length separate from win condition k ('in a row')
        self.win_condition = win_condition
        self.board_state = np.zeros((self.board_length, self.board_length))
        self.board_items_maximum = board_length*board_length

    def reset_board(self):
        self.board_state = np.zeros((self.board_length, self.board_length))
        self.winner = None
        self.game_over = False

    def reward(self):
        if self.game_over == True:
            return 1
        else:
            return -1

    # Checking to see if there's a tie or anyone has won the game
    # TODO, IF, THEN ITERATE. Right now board length must == in-a-row.
    def episode_resolution(self):
        for i in range(self.board_length):
            # horizontal winner?
            if abs(np.sum(self.board_state[i])) == self.win_condition:
                self.winner = True
                self.game_over = True
                if verbose == True : print('\n', 'horizontal win', self.game_over)
                return True

            # vertical winner?
            elif abs(np.sum(self.board_state[:,i])) == self.win_condition:
                self.winner = True
                self.game_over = True
                if verbose == True : print('\n', 'vertical win', self.game_over)
                return True
                
            # diagonal winner? \\ top left to bottom right
            elif abs(np.trace(self.board_state)) == self.win_condition: 
                self.winner = True
                self.game_over = True
                if verbose == True : print('\n', 'diagonal win \\ ', self.game_over)
                return True

            # diagonal winner? // top right to bottom left
            elif abs(np.trace(np.fliplr(self.board_state))) == self.win_condition: 
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
            # TODO Reward returns a negative value if no win condition met
            # future_state.winner == True
            # TODO Positive reward if there is a win condition
            if future_state.episode_resolution() == True:
                current_move = i
                # end loop if a good move has been found
                break
            else:
                future_state.board_state[i[0], i[1]] = 0
        # If no best move found, return a random move
        current_move = random.choice(legal_moves)
        return current_move
            
    def take_action(self, env):
        current_move = self.evaluate_move(env)
        env.board_state[current_move[0],current_move[1]] = self.player


# -------------------------------

# TODO, make this into a class object, iterations, environment, and agent as inputs
def game_iterations(iterations):
    for i in range(iterations):
        # Ann always goes first, tough shit for Bob.
        current_player = player_ann.player
        while env.game_over == False:
            if current_player == player_ann.player:
                player_ann.take_action(env)
                if verbose == True : print(env.board_state, 'ann just made move \n')
                # Check to see if the game is over
                if env.episode_resolution() == True:
                    if verbose == True : print('\n', 'Game Over!', env.episode_resolution(), '\n')
                    break
                # Now it's Bob's turn
                current_player = player_bob.player
            if current_player == player_bob.player:
                player_bob.take_action(env)
                if verbose == True : print(env.board_state, 'bob just made move \n')
                # Check to see if the game is over
                if env.episode_resolution() == True:
                    if verbose == True : print('\n', 'Game Over!', env.episode_resolution(), '\n')
                    break
                # Now it's Ann's turn
                current_player = player_ann.player
        # Who won this iteration?
        if verbose == True : print('Agent', current_player, ', won')
        print(env.board_state, '\n\n')
        # TODO, reduce this duplication and make it not suck.
        player_ann.state_history.append(('Tie?',not env.winner, 'last player to move', current_player))
        # player_bob.state_history.append(('Tie?',not env.winner, 'last player to move', current_player))
        # Reset the board
        env.reset_board()


random.seed(0)
verbose = True
env = Environment(3, 3)
player_ann = Agent(-1)
player_bob = Agent(1)

game_iterations(12)

for i in player_ann.state_history:
    print(i)
