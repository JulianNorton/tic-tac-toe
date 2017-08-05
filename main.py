import numpy as np
import human

print('test2')

board_length = 3

# agent_1 = agent.agent(.01,.01)

# c = agent.setV(b,5)

# ENVIRONMENT
class Environment:
    def __init__(self, board_length):
        self.board = np.zeros((board_length, board_length))
        self.player_one = -1 # 'x'
        self.player_two = 1 # '0'
        self.winner = None
        self.ended = False
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
        self.winner = None
        self.ended = False
        return False

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

    def reward(self, player_symbol):
        # no reward until game is over
        if not self.game_over():
            return 0
        # if game over
        if self.winner == player_symbol:
            return 1 
        else:
            return 0

def get_state_hash_and_winner(env, i=0, j=0):
    results = []

    for v in (0, env.player_one, env.player_two):
        env.board[i,j] = v # if empty board it should already be 0
        if j == 2:
            # j goes back to 0, increase i, unless i = 2, then we are done
            if i == 2:
                # the board is full, collect results and return
                state = env.get_state()
                ended = env.game_over(force_recalculate=True)
                winner = env.winner
                results.append((state, winner, ended))
            else:
                results += get_state_hash_and_winner(env, i + 1, 0)
        else:
            # increment j, i stays the same
            results += get_state_hash_and_winner(env, i, j + 1)

    return results



# -----------------------------------------------------------
# -----------------------------------------------------------
# AGENT
class Agent:
    def __init__(self, eps=0.1, alpha=0.5):
        self.eps = eps # probability of choosing random action instead of greedy
        self.alpha = alpha # learning rate
        self.verbose = False
        self.state_history = []
    
    def setV(self, V):
        self.V = V

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_verbose(self, v):
        # if true, will print(values for each position on the board)
        self.verbose = v

    def reset_history(self):
        self.state_history = []

    def take_action(self, env):
        # choose an action based on epsilon-greedy strategy
        r = np.random.rand()
        best_state = None
        if r < self.eps:
            # take a random action
            print("Taking a random action")

            possible_moves = []
            for i in range(board_length):
                for j in range(board_length):
                    if env.is_empty(i, j):
                        possible_moves.append((i, j))
            idx = np.random.choice(len(possible_moves))
            next_move = possible_moves[idx]
        else:
            # choose the best action based on current values of states
            # loop through all possible moves, get their values
            # keep track of the best value
            pos2value = {} # for debugging
            next_move = None
            best_value = -1
            for i in range(board_length):
                for j in range(board_length):
                    if env.is_empty(i, j):
                        # what is the state if we made this move?
                        env.board[i,j] = self.symbol
                        state = env.get_state()
                        env.board[i,j] = 0 # don't forget to change it back!
                        pos2value[(i,j)] = self.V[state]
                        if self.V[state] > best_value:
                            best_value = self.V[state]
                            best_state = state
                            next_move = (i, j)

            # if verbose, draw the board w/ the values
            if self.verbose:
                print("Taking a greedy action")
                for i in range(board_length):
                    print("-----------------")
                    for j in range(board_length):
                        if env.is_empty(i, j):
                            # print(the value)
                            print("%.2f|" % pos2value[(i,j)],)
                        else:
                            print(" ",)
                            if env.board[i,j] == env.x:
                                print("x |",)
                            elif env.board[i,j] == env.o:
                                print("o |",)
                            else:
                                print("  |",)
                    print('\n')
                print("-----------------")

        # make the move
        env.board[next_move[0], next_move[1]] = self.symbol
            

# def moves_selection(player):
#     possible_moves = moves_validate()
#     if len(possible_moves) > 0:
#         select_move = random.choice(moves_validate())
#         print(select_move)
#         select_move = list(select_move)
#         board[select_move[0],select_move[1]] = player
#         print('(',player,')', 'making a move!')
#     else:
#         print('no valid moves')

# set Values
# set symbols, give agent player value
# Set verbose, prints more information if True
# Reset history, start a new episode
# Take action, takes in environment as input.
# Update state history, updated when ANY player takes a turn.
# Update [only end of episode]
# -----------------------------------------------------------


# -----------------------------------------------------------
### PLAYING THE GAME
# -----------------------------------------------------------

def initialV_x(env, state_winner_triples):
    # initialize state values as follows
    # if x wins, V(s) = 1
    # if x loses or draw, V(s) = 0
    # otherwise, V(s) = 0.5
    V = np.zeros(env.board_permutations)
    for state, winner, ended in state_winner_triples:
        if ended:
            if winner == env.player_one:
                v = 1
            else:
                v = 0
        else:
            v = 0.5
        V[state] = v
    return V


def initialV_o(env, state_winner_triples):
    # this is (almost) the opposite of initial V for player x
    # since everywhere where x wins (1), o loses (0)
    # but a draw is still 0 for o
    V = np.zeros(env.board_permutations)
    for state, winner, ended in state_winner_triples:
        if ended:
            if winner == env.player_two:
                v = 1
            else:
                v = 0
        else:
            v = 0.5
        V[state] = v
    return V

def play_game(player_one, player_two, env, display=False):
    # loops until game is over
    current_player = None
    while not env.game_over():
        # alternate between players
        # p1 always first
        if current_player == player_one:
            current_player == player_two
        else:
            current_player == player_one

        # current player makes a move
        current_player.take_action()

        # update state histories
        state = env.get_state()
        player_one.update_state_history(state)
        player_two.update_state_history(state)

        # do the value function update
        player_one.update(env)
        player_two.update(env)

if __name__ == '__main__':
    # train the agent
    player_one = Agent(.01,.01)
    player_two = Agent(.01,.01)

    # set initial values for V for players
    env = Environment(board_length)
    state_winner_triples = get_state_hash_and_winner(env)

    Vx = initialV_x(env, state_winner_triples)
    player_one.setV(Vx)
    Vo = initialV_o(env, state_winner_triples)
    player_two.setV(Vo)

    # assign symbols to players
    player_one.set_symbol(env.player_one)
    player_two.set_symbol(env.player_two)


episodes = 1
for e in range(episodes):
    if e % 200 == 0:
        print(e)
    play_game(player_one, player_two, env)






