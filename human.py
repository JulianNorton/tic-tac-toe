class Human:
    def __init__(self):
        pass

    def set_symbol(self, symbol):
        self.symbol = symbol

    def take_action(self, env):
        while True:
            move = input('enter coordinates as "i,j"')
            i, j = move.split(',')
            i = int(i)
            j = int(j)
            if env.is_empty(i,j):
                env.board[i,j] = self.symbol
                break

    def update(self, env):
        pass
        
    def update_state_history(self, s):
        pass
