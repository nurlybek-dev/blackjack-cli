from game import Game

def main():
    players = 0
    while players < 1 or players > 7:
        players = int(input("How many players? (1-7): "))

    names = list()
    for _ in range(players):
        names.append(input("Enter player name: "))

    game = Game(names)

    again = 'y'

    while again != 'n' and again != 'N':
        game.play()
        again = input('Do you want to play again? (Y/N): ')


if __name__ == '__main__':
    main()