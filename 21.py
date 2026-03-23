



import random
# Global Configurations
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
}

deck = []
def create_deck():
    for suit in suits:
        for rank in ranks:
            deck.append([rank, suit])
    return deck

deck = create_deck()
print(deck)


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def deal_card(deck):
    """Removes and returns the top card from the deck."""
    # TODO: Return a card and handle the edge case of an empty deck
    pass

def calculate_score(hand):
    """
    Calculates the total value of cards in a hand.
    Requirement: If the score is over 21 and the hand contains an Ace, 
    reduce the score by 10 until the score is <= 21 or no Aces remain.
    """
    # TODO: Implement scoring logic and Ace adjustment
    pass

def show_hand(player_name, hand, hide_first_card=False):
 """Prints the formatted hand and current score for the user."""
    # TODO: Print cards. If hide_first_card is True, obscure the first card.
pass

def play_game():
    """Main game loop managing turns, user input, and winner logic."""
    # TODO: Implement game flow
    pass

if __name__ == "__main__":
    play_game()
