from card import Card
import itertools


class Deck:
    faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    __new_id = 0

    def __init__(self):
        self.cards = [Card(face, suit) for face, suit in itertools.product(Deck.faces, Deck.suits)]
        self.id = Deck.__new_id
        Deck.__new_id += 1

    def get_counts(self):
        counts_dict = {}
        for val in Deck.faces:
            counts_dict[val] = sum(card.face == val for card in self.cards)
        return counts_dict

    def __str__(self):
        return str([str(card) for card in self.cards])


if __name__ == '__main__':
    inst1 = Deck()
    print(inst1)
    print(inst1.get_counts())

