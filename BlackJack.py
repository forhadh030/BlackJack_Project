from random import shuffle


class Deck:
    """
Class representing the deck
    """
    def __init__(self):
        """
Initialize the deck and shuffle it.
        """
        suits = ['spade', 'club', 'diamond', 'heart']
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.deck = []
        for i in suits:
            for j in values:
                self.deck.append((i, j))
        shuffle(self.deck)

    def draw(self):
        """
Draw one card from the deck and return the drawn card.
        """
        return self.deck.pop(0)


class Person:
    """
Class representing the player
    """
    def __init__(self):
        """
Initialize your hand.
        """
        self.hands = []
        self.point = 0

    def add(self, card):
        """
Add a card to your hand.
        """
        self.hands.append(card)

    def point_sum(self):
        """
Find the total score of playing cards.
        """
        self.point = 0
        for i in self.hands:
            if i[1] in ['J', 'Q', 'K']:
                self.point += 10
            elif i[1] in ['A']:
                self.point += 11
            else:
                self.point += i[1]

        return self.point


def run():
    """
Main processing
    """
    print('Welcome to Blackjack!')

    d = Deck()
    p = Person()
    c = Person()

    drawing(d, p, 'you')
    drawing(d, p, 'you')

    drawing(d, c, 'CPU')
    card = d.draw()
    c.add(card)

    player_point = p.point_sum()
    cpu_point = c.point_sum()

    if player_point == cpu_point == 21:
        print("It's a draw.")
        return
    elif player_point == 21:
        print('You win!')
        return
    elif cpu_point == 21:
        print('You lose.')
        return

    while True:
        choice = input('Make your decision, "Hit" Or "Stand": ')

        while True:
            if choice.lower() == 'hit' or choice.lower() == 'stand':
                break
            else:
                choice = input('Make your decision, "Hit" Or "Stand": ')

        if choice.lower() == 'hit':
            drawing(d, p, 'you')
            player_point = p.point_sum()
            if player_point >= 22:
                print('You lose.')
                return
        elif choice.lower() == 'stand':
            break
        else:
            print('error')
            return

    print('CPU draws {} of {}'.format(c.hands[1][1], c.hands[1][0]))

    while True:
        cpu_point = c.point_sum()
        if cpu_point < 17:
            drawing(d, c, 'CPU')
            cpu_point = c.point_sum()
            if cpu_point >= 22:
                print('You win!')
                return
        else:
            break

    if player_point == cpu_point:
        print("It's a draw.")
        return
    elif player_point > cpu_point:
        print('You win!')
        return
    elif player_point < cpu_point:
        print('You lose.')
        return


def drawing(class1, class2, name):
    """
Add 1 card from the deck to your hand.
After that, the information of the added card is displayed.
    """
    card = class1.draw()
    class2.add(card)
    print('{} drew {} of {}'.format(name, card[1], card[0]))


run()