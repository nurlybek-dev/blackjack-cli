from hand import Hand


class GenericPlayer(Hand):
    def __init__(self, name):
        super(GenericPlayer, self).__init__()
        self.name = name
    
    def is_hitting(self):
        pass

    def is_busted(self):
        return self.total() > 21

    def bust(self):
        print(self.name, 'busts.')

    def print_hand(self):
        print(self.name, end='\t')
        if self.cards:
            for card in self.cards:
                print(card, end='\t')
            if self.total() != 0:
                print('(',self.total(),')', sep='')
        else:
            print('<empty>')
