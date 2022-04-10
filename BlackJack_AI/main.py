from game import Game
from rewards_ai import RewardsAI
import random
import pandas as pd


def main():
    random.seed(1)  # Seed 4 has an ace # Seed 21 is blackjack for gambler
    rewarding_ai = RewardsAI(trials=100)
    game = Game(1, 6, True, rewarding_ai)
    iters = int(1 * 10 ** 6)
    for iter in range(iters):
        game.play_round()
        if iter % 10 ** 5 == 0:
            print(len(rewarding_ai.states_hashdict))
            print(iter)
            print(f"Winrate of AI is : {rewarding_ai.get_winrate()}")
    print(f"Winrate of AI is : {rewarding_ai.get_winrate()}")
    df = pd.DataFrame(data=rewarding_ai.states_hashdict)
    df = df.T
    df.to_excel("Runs_1e6_iters.xlsx")


if __name__ == '__main__':
    main()
    print("")
