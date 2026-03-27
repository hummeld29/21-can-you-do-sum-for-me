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
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append([rank, suit])
    return deck

deck = create_deck()


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def deal_card(deck):

    return deck.pop(0) 

card1 = deal_card(deck)
card2 = deal_card(deck)
hand = [ card1, card2]


def calculate_score(hand):
        score = 0
        ace_count = 0   
        for card in hand:
            rank = card[0]
            score  += values[rank]
            if rank == "Ace":
                ace_count += 1
        while score > 21 and ace_count > 0:
            score -= 10
            ace_count -= 1
        return score 






"""
    #Calculates the total value of cards in a hand.
    Requirement: If the score is over 21 and the hand contains an Ace, 
    reduce the score by 10 until the score is <= 21 or no Aces remain.
    """
player_name = input("whats your name:")
hide_first_card = False
def show_hand(player_name, hand, hide_first_card = False):
    cards = ["??" if hide_first_card and card == hand[0] else f"{card[0]} of {card[1]}"for card in hand]
    score = f" | Score: {calculate_score(hand)}" if not hide_first_card else ""
    print(f"{player_name}'s hand: {', '.join(cards)}{score}")
  


def play_game():
    while True:
        deck = create_deck()
        shuffle_deck(deck)
        hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]

        while True:
            dealer_score = calculate_score(dealer_hand)
            player_score = calculate_score(hand)

            show_hand("player", hand)
            show_hand("dealer", dealer_hand, hide_first_card=True)

            if len(deck) < 20:
                print("deck is empty. reshuffling.")
                deck = create_deck()
                shuffle_deck(deck)

            if player_score > 21:
                print("you busted. dealer wins the round.")
                break
            elif player_score == 21:
                print("blackjack u win")
                break

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
                    show_hand(player_name, hand)
                    if dealer_score > 21:
                        print("dealer busted. you win the round.")
                    elif dealer_score > player_score:
                        print("dealer wins the round.")
                    elif dealer_score < player_score:
                        print("you win the round.")
                    else:
                        print("it's a tie!")
                    break
                else:
                    print("invalid input. please type 'hit' or 'stand'.")   
                
        






    """Main game loop managing turns, user input, and winner logic."""
    # TODO: Implement game flow
play_game()