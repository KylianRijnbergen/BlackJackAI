from deck import Deck
import random


class Shoe:
    __new_id = 0

    def __init__(self, num_decks, cards=None):
        self.num_decks = num_decks
        self.id = Shoe.__new_id
        Shoe.__new_id += 1
        if cards is None:
            decks = [Deck() for _ in range(self.num_decks)]
            self.cards = [card for deck in decks for card in deck.cards]

    def get_counts(self):
        counts_dict = {}
        for val in Deck.faces:
            counts_dict[val] = sum(card.face == val for card in self.cards)
        return counts_dict

    def deal(self):
        return self.cards.pop(random.randrange(len(self.cards)))

    def __str__(self):
        return f"{[str(card) for card in self.cards]}"


if __name__ == '__main__':
    inst1 = Shoe(6)
    print(inst1)
    print("")
