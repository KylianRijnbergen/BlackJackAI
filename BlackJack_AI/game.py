from player import Dealer, Gambler
from shoe import Shoe
import random


class Game:
    __new_id = 0

    def __init__(self, num_gamblers=1, num_decks=6, auto=False, AI=None):
        self.dealer = Dealer()
        self.num_gamblers = num_gamblers
        self.gamblers = [Gambler(funds=100) for _ in range(self.num_gamblers)]
        self.num_decks = num_decks
        self.shoe = Shoe(self.num_decks)
        self.shoe_count = 0
        self.auto = auto
        self.id = Game.__new_id
        self.ai = AI
        Game.__new_id += 1

    def get_card(self):
        return self.shoe.cards.pop(random.randrange(len(self.shoe.cards)))

    def deal(self):
        for _ in range(2):
            self.dealer.add_card(self.get_card())
            for gambler in self.gamblers:
                gambler.add_card(self.get_card())

    def play_round(self):
        # If there is less than 52 cards in the shoe, we must shuffle. This results in a new shoe count of 0.
        if len(self.shoe.cards) < 52:
            self.shoe = Shoe(self.num_decks)
            self.shoe_count = 0
            if not self.auto:
                print("Shoe is reset as there were less than 52 cards left in the shoe.")
        self.deal()
        if not self.auto:
            pass
        #print(self.dealer)
        for gambler in self.gamblers:
            stt, actn = self.play_gambler(gambler)

        # Now, we play the dealer.
        dealer_pts = self.play_dealer()

        # We store the decisions the players made.
        player_decisions = []
        # Blackjack pays 3 to 2.
        for gambler in self.gamblers:
            round_result = None
            gambler_pts = gambler.get_points()
            # Gambler wins if gambler has more points than dealer, and neither is busted,
            # Or dealer is busted and gambler is not.
            if 21 > gambler_pts > dealer_pts or gambler_pts < 21 < dealer_pts:
                round_result = "Gambler won"
            # Gambler wins by blackjack if gambler has 21 and dealer is busted.
            elif 21 == gambler_pts > dealer_pts or gambler_pts == 21 < dealer_pts:
                round_result = "Gambler won by blackjack"
            else:
                round_result = "Dealer won"
            if not self.auto:
                pass#print(round_result)
            player_decisions.append(gambler.decisions)

            # Add state to the AI's memory
            self.ai.add_state(stt, actn, round_result)

        # At the end of the round, we update the shoe count.
        self.get_shoe_count()
        # At the end of the round, we reset the hands of the players. We also reset decisions.
        for gambler in self.gamblers:
            gambler.hand = []
            gambler.decisions = ["s"]
        # We also reset the hand of the dealer.
        self.dealer.hand = []

    def play_gambler(self, gambler):
        if not self.auto:
            pass
        #print(gambler)
        # Do a while loop until the player can no longer hit.
        (bool_, stt, actn) = self.get_action(gambler)
        while bool_:
            gambler.add_card(self.get_card())

            #print("HIT!")
            # If player hit, we add this as a decision
            (bool_, stt, actn) = self.get_action(gambler)
            if not self.auto:
                pass
            #print(gambler)
            print(type(stt), type(actn))
            return stt, actn

    def play_dealer(self):
        if not self.auto:
            self.dealer.show_hand()
        while self.dealer.get_points() < 17:
            self.dealer.add_card(self.get_card())
            if not self.auto:
                self.dealer.show_hand()
        return self.dealer.get_points()

    def get_shoe_count(self):
        # We update the shoe count and store it in self.shoe_count
        for gambler in self.gamblers:
            for card in gambler.hand:
                if card.get_pts() <= 6:
                    self.shoe_count += 1
                elif 7 <= card.get_pts() <= 9:
                    pass
                else:
                    self.shoe_count -= 1
        for card in self.dealer.hand:
            if card.get_pts() <= 6:
                self.shoe_count += 1
            elif 7 <= card.get_pts() <= 9:
                pass
            else:
                self.shoe_count -= 1

    def get_state(self, gambler):
        # This returns the state of the game. State consists of dealer card value, player card value, player num aces, and shoe count.
        return f"{self.dealer.get_shown_points()}_{gambler.get_points()}_{gambler.get_aces()}_{self.shoe_count}"

    def get_action(self, gambler):
        state_ = self.get_state(gambler)
        # Return False on BlackJack
        if gambler.get_points() == 21:
            if not self.auto:
                print("Blackjack!")
            return (False, state_, gambler.decisions[-1])
        # Return False if player is busted
        if gambler.get_points() > 21:
            if not self.auto:
                print("Busted!")
            return (False, state_, gambler.decisions[-1])

        # Return False if player decides to stay
        chosen_input = None
        if self.auto:
            chosen_input = self.ai.choose(state_)
            self.gamblers[0].decisions.append(chosen_input)

        else:
            chosen_input = input("Stay or Hit? ['s', 'h'] ")

        print(type(state_), type(gambler.decisions[-1]))

        return (False, state_, gambler.decisions[-1]) if chosen_input == "s" else (True, state_, gambler.decisions[-1])


if __name__ == "__main__":
    gme = Game()
    print(gme)
