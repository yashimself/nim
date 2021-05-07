import time

class NimGame:
    def __init__(self, n):
        self.n = n

    def startState(self):
        return self.n

    def isEmpty(self, state):
        return True if state == 0 else False

    def utility(self, state, player):
        if state == 0:
            if player == 1:
                return float('-inf') # negative infinity
            else:
                return float('+inf') # positive infinity

    def actions(self, state):
        if state >= 3:
            return [1, 2, 3]
        return range(1, state + 1)

    def successor(self, state, withdrawn):
        if withdrawn > state:
            return 0
        return state - withdrawn


def minmax(game, state, player):

    def recursivecheck(state, player):

        if game.isEmpty(state) == True:
            return (game.utility(state, player), None) # i.e don't take any action
        if cache.has_key((state, player)): # check if the key is present in the dict
            return cache[(state, player)]

        # Check for all possible actions in the game 
        choices = [(recursivecheck(game.successor(state, withdrawn), -1 * player)[0], withdrawn) for withdrawn in game.actions(state)] 
        if player == +1: 
            val = max(choices) # maximise for self
        else:
            val = min(choices) # minimise for opponent
        cache[(state, player)] = val
        return val

    value, withdrawn = recursivecheck(state, player)
    return (value, withdrawn)


cache = {}

if __name__ == "__main__":

    game = NimGame(25)
    state = game.startState()
    print("\t\t\t **** Game starts ****")
    while (state > 0):
        withdrawn = 0
        print "\n **** There are ", state, "coins in the bag currently **** \n"
        while (withdrawn not in [1, 2, 3]) and state - withdrawn >= 0:
            withdrawn = int(input(" \n ----->YOUR TURN<----- \n\n Choose number of coins to withdraw: 1,2,3\n"))

        state -= withdrawn
        print "\n **** There are ", state, "coins in the bag currently **** \n"
        if state == 0:
            print("**** Congratulations! You won! ****")
            break
        val, act = minmax(game, state, 1)
        state -= act
        time.sleep(1)
        print " \n ----->COMPUTER'S TURN<----- \n\n Computer player withdrew", act," coins \n"
        time.sleep(2)
        if state == 0:
            print "**** Sorry you Lost! ****"
