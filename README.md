Objective
Build a command-line version of Card Clash 21. Practice professional development by using Git for version control, functions for modular programming, and defensive programming for edge cases like Ace values and invalid input.
Game Rules and Mechanics: Card Clash 21
To ensure players and developers understand the logic behind the code, the following rules govern the game. Card Clash 21 is a game of chance and strategy where the player competes against the computer (the Dealer).
The Goal
The objective is to have a hand value as close to 21 as possible without going over. If your hand exceeds 21, you "Bust" and automatically lose the round.
Card Values
Number Cards (2-10): Face value (e.g., a 7 is worth 7 points).
Face Cards (Jack, Queen, King): Each is worth 10 points.
Aces: Flexible value. An Ace is worth 11 points unless that would cause the hand to exceed 21, in which case it is worth 1 point.
Gameplay Flow
The Deal: Both the Player and the Dealer are dealt two cards. The Player can see both of their cards, but only one of the Dealer's cards is revealed.
The Player's Turn: * Hit: Take another card from the deck to increase your score. You can Hit as many times as you like until you Stand or Bust.
Stand: Keep your current total and end your turn.
The Dealer's Turn: Once the player stands, the Dealer reveals their hidden card. The Dealer must follow a strict rule: they must Hit until their total score is 17 or higher.
Determining the Winner:
If the Player busts, the Dealer wins immediately.
If the Dealer busts, the Player wins.
If neither busts, the person with the higher score wins.
If the scores are equal, the game ends in a Tie (Push).
Implementation Guide: The Logic of "The Soft Hand"
One of the most important logic hurdles in this lab is handling the Ace. In programming, this is often handled by calculating the maximum possible score first and then "correcting" it.
Sum all cards, counting every Ace as 11.
While the total is over 21 AND you still have an Ace that is being counted as 11:
Subtract 10 from the total.
Mark that Ace as "used" (count it as 1).
Repeat this until the score is 21 or lower, or you run out of Aces to convert
