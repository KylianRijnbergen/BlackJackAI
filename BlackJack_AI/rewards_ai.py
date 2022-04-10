import random


class RewardsAI:
    def __init__(self, trials=1000):
        self.states_hashdict = {}
        self.trials = trials
        self.wins = 0
        self.win_by_blackjack = 0
        self.loss = 0
        self.games = 0

    def add_state(self, state, decision, result):
        hash_state = state
        result_hash = result
        reward = 0
        if hash_state not in self.states_hashdict:
            self.states_hashdict[hash_state] = [["h", self.trials], ["s", self.trials], []]
        self.games += 1
        if result == "Gambler won":
            reward = 1
            if self.games > 10 ** 7:
                self.wins += 1
        if result == "Gambler won by blackjack":
            reward = 2
            if self.games > 10 ** 7:
                self.win_by_blackjack += 1
        if result == "Dealer won":
            if self.games > 10 ** 7:
                self.loss += 1
            reward = -1
        #print(result)

        if decision == "h":
            self.states_hashdict[hash_state][0][1] += reward
            if self.states_hashdict[hash_state][0][1] == 0:
                self.states_hashdict[hash_state][0][1] = 1
            if result_hash not in self.states_hashdict[hash_state][2]:
                self.states_hashdict[hash_state][2].append(result_hash)
        elif decision == "s":
            self.states_hashdict[hash_state][1][1] += reward
            if self.states_hashdict[hash_state][1][1] == 0:
                self.states_hashdict[hash_state][1][1] = 1
            if result_hash not in self.states_hashdict[hash_state][2]:
                self.states_hashdict[hash_state][2].append(result_hash)

    def get_winrate(self):
        return (self.wins + self.win_by_blackjack)/max(1, (self.wins + self.win_by_blackjack + self.loss))

    def choose(self, state):
        hash_state = state
        if hash_state not in self.states_hashdict:
            return random.choice(["h", "s"])
        else:
            prob_h = self.states_hashdict[hash_state][0][1]
            prob_s = self.states_hashdict[hash_state][1][1]
            return "h" if prob_h / (prob_h + prob_s) > random.random() else "s"

    def __str__(self):
        return str(self.states_hashdict)


if __name__ == "__main__":
    print("")
