# Object oriented programming - oop
import random


class Cards:

    def __init__(self, cards_total, shuffle_cards):
        self.cards_total = cards_total
        self.shuffle_cards = shuffle_cards

    def create_cards(self):
        for x in range(1, 53):
            self.cards_total.append(x)
            self.shuffle_cards.append(x)

    def shuffled_cards(self):
        random.shuffle(self.shuffle_cards)
        print(self.shuffle_cards)


class Players:

    def __init__(self):
        self.total_cards = []
        self.shuffled_cards = []
        self.cards = Cards(self.total_cards, self.shuffled_cards)

    def player1_cards(self):
        self.cards.create_cards()
        self.cards.shuffled_cards()
        print(self.cards.shuffle_cards[0:26])

    def player2_cards(self):
        print(self.cards.shuffle_cards[26:52])


class Game:

    def __init__(self):
        self.players = Players()

    def run(self):
        self.players.player1_cards()
        self.players.player2_cards()


if __name__ == "__main__":
    game = Game()
    game.run()

