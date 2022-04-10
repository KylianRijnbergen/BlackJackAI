class Card:
    __new_id = 0

    def __init__(self, face, suit=None):
        self.face = face
        self.suit = suit
        self.id = Card.__new_id
        Card.__new_id += 1

    def get_pts(self):
        if isinstance(self.face, int):
            return self.face
        elif self.face == "A":
            return 11
        else:
            return 10

    def __lt__(self, point_value):
        if self.get_pts() < point_value:
            return True
        return False

    def __gt__(self, point_value):
        if self.get_pts() > point_value:
            return True
        return False

    def __eq__(self, point_value):
        if self.get_pts() == point_value:
            return True
        return False


    def __str__(self):
        return f"{self.face} of {self.suit}"


if __name__ == '__main__':
    inst1 = Card(10)
