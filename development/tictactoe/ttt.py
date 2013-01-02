
class TicTacToe:
    
    UNBEGUN = -1
    ONGOING = 0
    ENDED = 1

    symbols = ["x", "o"]
    state = UNBEGUN
    last_player = -1
    turn = 0

    def __init__(self, width=3, height=3):
        self.width = width
        self.height = width
        self.grid = [[" "]*self.width]*self.height

    def play(self):
        while True:
            

    def move(self, player, x, y):
        if self.grid[y][x] != " ": return False
        elif x not in range(self.width): return False
        elif y not in range(self.height): return False
        else:
            self.grid[y][x] = self.symbols[player]
            self.last_player = player
            if self.check_win(player, x, y):
                self.state = self.ENDED
            return True

    def check_win(self, player, x, y):
        win = True

        # Check row
        for i in range(self.width):
            if self.grid[y][i] != self.symbols[player]:
                win = False

        # Check column
        for i in range(self.height):
            if self.grid[i][x] != self.symbols[player]:
                win = False

        # Check diagonals
        diag_len = self.height if self.height > self.width else self.width
        for i in range(diag_len):
            if self.grid[i][i] != self.symbols[player]:
                win = False
                return
            elif self.grid[i][diag_len-1-i] != self.symbols[player]:
                win = False

        return win
            
            

    def convert_coord(self, coord):
        if len(coord) != 2: return None
        x, y = -1, -1
        coord = coord.lower()
        if coord[1].isdigit():
            coord = coord[::-1]
        y = int(coord[0])
        x = ord(coord[1])-97
        return (x, y)
        
    def print_grid(self):
        grp = []
        for i in self.grid:
            tp = "|"
            for j in i:
                tp += "%s|" % j
            grp.append(tp)
        ret = "   a b c\n"
        for i in range(len(grp)):
            ret += "%d %s\n" % (i, grp[i])
        print ret[:-1]
        

    
def main():
    game = TicTacToe()
    game.print_grid()

if __name__ == "__main__":
    main()
