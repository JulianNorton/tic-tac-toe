import numpy as np
import environment
import agent
import human
import reward

print('test2')

# agent_1 = agent.agent(.01,.01)

# c = agent.setV(b,5)

def play_game(player_one, player_two, env, display=False):
    # loops until game is over
    current_player = None
    while not environment.game_over(False):
        # alternate between players
        # p1 always first
        if current_player == player_one:
            current_player == player_two
        else:
            current_player == player_one

        # to see what's going on
        if display:
            if draw == 1 and current_player == player_one:
                env.draw_board()
            if draw == 2 and current_player == player_two:
                env.draw_board()

        # current player makes a move
        current_player.take_action(env)

        # update state histories
        state = env.get_state()
        player_one.update_state_history(state)
        player_two.update_state_history(state)

        # see what's going on after actions
        if display:
            env.draw_board()

        # do the value function update
        player_one.update(env)
        player_two.update(env)


if __name__ == '__main__':
    # train the agent
    player_one = agent.agent(.01,.01)
    player_two = agent.agent(.01,.01)

    # set initial values for V for players
    env = environment.Environment(3)
    # state_winner_triples = environment.get_state_hash_and_winner(env)

    # Vx = initialV_x(env, state_winner_triples)
    # player_one.setV(Vx)
    # Vo = initialV_o(env, state_winner_triples)
    # player_two.setV(Vo)

    # assign symbols to players
    # player_one.set_symbol(env.x)
    # player_two.set_symbol(env.o)


episodes = 10000
for e in range(episodes):
    if e % 200 == 0:
        print(e)
    play_game(player_one, player_two, env)
