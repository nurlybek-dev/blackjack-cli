from deck import Deck
from house import House
from player import Player

class Game:
    def __init__(self, names):
        self.deck = Deck()
        self.house = House('house')
        self.players = list()
        for name in names:
            self.players.append(Player(name))

    def play(self):
        self.deck.check_cards_count()
        for _ in range(2):
            for player in self.players:
                self.deck.deal(player)
            self.deck.deal(self.house)
        self.house.flip_first_card()

        for player in self.players:
            player.print_hand()
        self.house.print_hand()

        for player in self.players:
            self.deck.additional_cards(player)
        self.deck.additional_cards(self.house)
        
        self.house.flip_first_card()
        self.house.print_hand()

        if self.house.is_busted():
            for player in self.players:
                if not player.is_busted():
                    player.win()
        else:
            for player in self.players:
                if not player.is_busted():
                    if player.total() > self.house.total():
                        player.win()
                    elif player.total() < self.house.total():
                        player.lose()
                    else:
                        player.push()
        
        for player in self.players:
            player.clear()
        self.house.clear()
