from card import Card


class Player:
    def __init__(self, hand=None):
        if hand is None:
            self.hand = []
        else:
            self.hand = hand

    def add_card(self, card):
        self.hand.append(card)

    def get_aces(self):
        num_aces = 0
        for card in self.hand:
            if card.face == "A":
                num_aces += 1
        return num_aces

    def get_points(self):
        pts = 0
        num_aces = self.get_aces()
        for card in self.hand:
            pts += card.get_pts()

        while pts > 21 and num_aces > 0:
            pts -= 10
            num_aces -= 1
        return pts


class Gambler(Player):
    __new_id = 0

    def __init__(self, funds=None):
        Player.__init__(self, hand=None)
        self.decisions = ['s']
        self.id = Gambler.__new_id
        self.funds = funds
        Gambler.__new_id += 1

    def add_funds(self, amount):
        self.funds += amount

    def remove_funds(self, amount):
        self.funds -= amount

    def show_hand(self):
        if not self.hand:
            print("Gambler has no cards.")
        else:
            print(f"Hand of gambler is [{self.hand}]. ")

    def __str__(self):
        return "Gambler has no cards." if not self.hand else f"Hand of gambler is {[str(card) for card in self.hand]}. This is worth {self.get_points()} points."


class Dealer(Player):
    __new_id = 0

    def __init__(self):
        Player.__init__(self, hand=None)
        self.id = Dealer.__new_id
        Dealer.__new_id += 1

    def get_shown_points(self):
        return self.hand[0].get_pts()

    def show_hand(self):
        if not self.hand:
            print("Dealer has no cards.")
        else:
            print(f"Hand of dealer is {[str(card) for card in self.hand]}. This is worth {self.get_points()} points.")

    def __str__(self):
        return "Dealer has no cards." if not self.hand else f"Hand of dealer is [X, {str([str(card) for card in self.hand[1:]])[1:]}."


if __name__ == '__main__':
    inst1 = Gambler()
    print(inst1.hand)
    inst1.show_hand()
    inst2 = Dealer()
    inst2.show_hand()
    print("")
