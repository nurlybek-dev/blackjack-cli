import random

from hand import Hand
from card import Card, Rank, Suit


class Deck(Hand):
    def __init__(self):
        super(Deck, self).__init__()

    def populate(self):
        self.clear()
        for s in range(Suit.CLUBS, Suit.SPADES):
            for r in range(Rank.ACE, Rank.KING):
                self.add(Card(r, s))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hand):
        if self.cards:
            hand.add(self.cards.pop())
        else:
            print('Out of cards. Unable to deal.')

    def additional_cards(self, generic_player):
        while not generic_player.is_busted() and generic_player.is_hitting():
            self.deal(generic_player)
            generic_player.print_hand()
            if generic_player.is_busted():
                generic_player.bust()

    def check_cards_count(self):
        if len(self.cards) < 10:
            self.populate()
            self.shuffle()

