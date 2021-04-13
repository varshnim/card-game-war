import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    """
    A class for a playing card
    Takes the suit and rank as input params
    Calculates a numerical value to the card
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    """
    Class for a deck of cards
    Creates a fresh deck based on the global variables suits and ranks
    Has methods to shuffle the created deck and to deal a single card
    """

    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()


class Player:
    """
    Class for a player
    Takes the player name as param during instantiation
    Can hold a set of cards as param all_cards
    Can remove one card using method remove_one()
    Can add one or more cards using the add_cards() method
    """

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


def create_player():
    """
    Create player instance
    :return: instance of Player class
    """
    return Player(input("Enter Player Name: "))


def deal_to_players(shuffled_deck):
    """
    Deal the shuffled deck to the players
    :param shuffled_deck: shuffled deck
    """
    for i in range(26):
        p1.add_cards(shuffled_deck.deal_one())
        p2.add_cards(shuffled_deck.deal_one())


if __name__ == '__main__':
    # Calling Class
    print("PLAYER 1")
    p1 = create_player()
    print("PLAYER 2")
    p2 = create_player()

    # Create and shuffle a deck
    new_deck = Deck()
    new_deck.shuffle()

    # Deal to players
    deal_to_players(new_deck)

    game_over = False

    round_counter = 0
    while not game_over:
        round_counter += 1
        print(f"--Round {round_counter}--")

        # Drawing a card for player 1
        if len(p1.all_cards) > 0:
            p1_playing_card = []
            p1_playing_card.append(p1.remove_one())
        else:
            print(f"{p1.name} doesn't have cards left to play. {p2.name} wins!")
            game_over = True
            break

        # Drawing a card for player 2
        if len(p2.all_cards) > 0:
            p2_playing_card = []
            p2_playing_card.append(p2.remove_one())
        else:
            print(f"{p2.name} doesn't have cards left to play. {p1.name} wins!")
            game_over = True
            break

        war_on = True
        while war_on:
            # If player 2 has a higher value card
            if p1_playing_card[-1].value < p2_playing_card[-1].value:
                p1.add_cards(p1_playing_card)
                p1.add_cards(p2_playing_card)
                war_on = False

            # If player 1 has a higher value card
            elif p1_playing_card[-1].value > p2_playing_card[-1].value:
                p2.add_cards(p1_playing_card)
                p2.add_cards(p2_playing_card)
                war_on = False

            else:
                print("!!!WAR!!!")

                if len(p1.all_cards) < 5:
                    print(f"{p1.name} doesn't have enough cards to go to war! {p2.name} wins!")
                    game_over = True
                    break
                elif len(p2.all_cards) < 5:
                    print(f"{p2.name} doesn't have enough cards to go to war! {p1.name} wins!")
                    game_over = True
                    break
                else:
                    for i in range(5):
                        p1_playing_card.append(p1.remove_one())
                        p2_playing_card.append(p2.remove_one())
