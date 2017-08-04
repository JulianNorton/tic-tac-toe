def reward(self, player_symbol):
    # no reward until game is over
    if not self.game_over():
        return 0
    # if game over
    if self.winner == player_symbol:
        return 1 
    else:
        return 0