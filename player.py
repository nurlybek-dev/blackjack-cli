from generic_player import GenericPlayer


class Player(GenericPlayer):
    def __init__(self, name):
        super(Player, self).__init__(name)

    def is_hitting(self):
        responce = input(f'{self.name} do you want a hit? (Y/N): ')
        return responce == 'Y' or responce == 'y'

    def win(self):
        print(self.name, 'wins.')

    def lose(self):
        print(self.name, 'loses.')

    def push(self):
        print(self.name, 'pushes.')
