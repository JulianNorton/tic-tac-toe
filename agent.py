class Agent:
    def __init__(self, epsilon, alpha):
        self.epsilon = epsilon # probability of choosing random action
        self.alpha = alpha # learning rate for update equation
        self.verbose = False # debugging
        self.state_history = [] # empty list for an open mind

def setV(self, V):
    self.V = V

def set_symbol(self, symbol):
    self.symbol = symbol

def set_verbose(self, v):
    self.verbose = v

def reset_history(self):
    self.state_history = []

def take_action(self, env):
    # determine to take action based on epsilon-greedy strategy
    # random float between 0-1
    random_action = np.random.rand()
    best_state = None
    moves_available = moves_validate()
    if random_action < self.epsilon:
        # taking a random action
        if self.verbose:
            print('random action!')
        # How many choices are available?
        move_selection = np.random.choice(len(moves_available))
        # Select a choice from moves available
        move_selection = list(moves_available[move_selection])
    else:
        pos2value = {} # for debugging
        move_selection = None
        best_value = -1
        for i in range(board_length):
            for j in range(board_length):
                if env.is_empty(i,j):
                    # what is the state if we made this move?
                    env.board[i,j] = self.symbol
                    state = env.get_state()
                    env.board[i,j] = 0 # change move back to 0
                    pos2value[(i,j)] = self.V[state]
                    if self.V[state] > best_value:
                        best_value = self.V[state]
                        best_state = state
                        next_move = (i,j)
        if self.verbose:
            print('taking a greedy action')


def update_state_history(self, s):
    '''
    cannot put this in take_action because take_action only happens
    once every other iteration per player
    state history needs to be updated *every* iteration
    s = env.get_state() # don't want to do it twice so pass it in
    '''
    self.state_history.append(s)

def update(self, environment):
    '''
    we want to backtrack over the states so that:
    V(prev_state) = V(prev_state) + alpha*(V(next_state)) - V(prev_state))
    where V(next_state) = reward if it's the most current state
    Note we only do this at the end of the episode
    not so for all algorithms we will study
    '''
    reward = env.reward(self.symbol)
    target = reward
    for prev in reversed(self.state_history):
        value = self.V[pref] + self.alpha*(target - self.V[prev])
        self.V[prev] = value
        target = value
    self.reset_history()

        

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


