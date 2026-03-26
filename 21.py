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


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def deal_card(deck):

    deck.pop(0) 

card1 = deal_card(deck)
card2 = deal_card(deck)
hand = [ card1, card2]

def calculate_score(hand):
        score = 0
        for card in hand:
            rank = card[0]
            value  += value[card]
            if rank == "Ace":
                acecout += 1
        while score > 21 and ace_count > 0:
            score -= 10
            ace_count -= 1
        return score 






"""
    #Calculates the total value of cards in a hand.
    Requirement: If the score is over 21 and the hand contains an Ace, 
    reduce the score by 10 until the score is <= 21 or no Aces remain.
    """
    # TODO: Implement scoring logic and Ace adjustment

def show_hand(player_name, hand, hide_first_card=False):
 print( f"{player_name}'s hand: , score is {calculate_score(hand)}")

 

 """Prints the formatted hand and current score for the user."""
    # TODO: Print cards. If hide_first_card is True, obscure the first card.
pass

def play_game():
    deck = create_deck()
    shuffle_deck(deck)
    card1 = deal_card(deck)
    card2 = deal_card(deck)
    hand = calculate_score([card1, card2])
    dealer_card1 = deal_card(deck)
    dealer_card2 = deal_card(deck)
    dealer_hand = [dealer_card1, dealer_card2]
    dealer_score = calculate_score(dealer_hand)
    while True:
        show_hand("your", hand)
        print(f"dealer's hand: {dealer_card1} and a hidden card" )
        if hand > 21:
            print("you busted. dealer wins the round.")
            continue
        elif hand == 21:
            print("blackjack u win")
            continue
        else:
            user_input = input("type 'hit' to get another card, or 'stand' to hold your hand: ")
            if user_input.lower() == "hit":
                new_card = deal_card(deck)
                hand.append(new_card)
            elif user_input.lower() == "stand":
                while dealer_score < 17:
                    new_card = deal_card(deck)
                    dealer_hand.append(new_card)
                    dealer_score = calculate_score(dealer_hand)
                show_hand("dealer's", dealer_hand)
                if dealer_score > 21:
                    print("dealer busted. you win the round.")
                elif dealer_score > hand:
                    print("dealer wins the round.")
                elif dealer_score < hand:
                    print("you win the round.")
                else:
                    print("it's a tie!")
                break
            else:
                print("invalid input. please type 'hit' or 'stand'.")   
                
        






    """Main game loop managing turns, user input, and winner logic."""
    # TODO: Implement game flow
play_game()
