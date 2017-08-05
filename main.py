import numpy as np
import environment
import agent
import reward

print('test2')

# agent_1 = agent.agent(.01,.01)

# c = agent.setV(b,5)

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

        if display == true:
            print('test')