import math, sys

class NimGame:
    def __init__(self, heap_state=10, players=2):
        self.heap_state = heap_state
        self.players = players
        self.current_turn = -1

    def get_guess(self):
        while True:
            guess = raw_input("It's player %d's turn to pick: " % (self.current_turn + 1))
            if guess.isdigit():
                root_guess = math.sqrt(float(guess))
                if root_guess == math.floor(root_guess):
                    if self.heap_state - int(guess) >= 0:
                        return int(guess)
                    else:
                        print "The heap size may not negative after guess. Repick."
                else:
                    print "That's not a square. Repick."
            else:
                print "That's not an integer. Repick."

    def report_heap(self):
        print "The heap contains %d." % self.heap_state
        
    def play(self):
        while self.heap_state != 0:
            self.report_heap()
            self.current_turn = (self.current_turn + 1) % self.players
            guess = self.get_guess()
            self.heap_state = self.heap_state - guess
        print "Player %d loses!" % (self.current_turn + 1)

def main():
    heap_size = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    nim = NimGame(heap_size, 3)
    nim.play()

if __name__ == "__main__":
    main()
