import time

class NimGame:
    def __init__(self, n):
        self.n = n

    def startState(self):
        return self.n

    def isEnd(self, state):
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

    def successor(self, state, action):
        if action > state:
            return 0
        return state - action


def minmax(game, state, player):

    def recurse(state, player):

        if game.isEnd(state) == True:
            return (game.utility(state, player), None) # i.e don't take any action
        if cache.has_key((state, player)): # check if the key is present in the dict
            return cache[(state, player)]

        # Check for all possible actions in the game 
        choices = [(recurse(game.successor(state, action), -1 * player)[0], action) for action in game.actions(state)] 
        if player == +1: 
            val = max(choices) # maximise for self
        else:
            val = min(choices) # minimise for opponent
        cache[(state, player)] = val
        # print val
        return val

    value, action = recurse(state, player)
    return (value, action)


cache = {}

if __name__ == "__main__":

    game = NimGame(25)
    state = game.startState()
    print("\t\t\t **** Game starts ****")
    while (state > 0):
        action = 0
        print "\n **** There are ", state, "coins in the bag currently **** \n"
        while (action not in [1, 2, 3]) and state - action >= 0:
            action = int(input(" \n ----->YOUR TURN<----- \n\n Choose number of coins to withdraw: 1,2,3\n"))

        state -= action
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
