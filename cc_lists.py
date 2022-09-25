""" 
Begin by creating a new file with a .py extension (for example, lists_challenge.py) and adding the following code to it:
import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
This last line that says "while diamonds:" will begin a while loop that will iterate as long as the diamonds list is not empty.
Your challenge begins inside the while loop:
Prompt the user to input either enter to pick a card, or Q plus enter to quit.
If the user input is "Q" then break out of the while loop.
Otherwise, think of a way to use a method from the random module such that a random card is selected from the diamonds list.
Use list methods to remove that card from the diamonds list, then add it to the hands list.
Print the contents of both decks. 
After the while loop ends, use an if statement to check the condition not diamonds like so:
if not diamonds:
This statement will evaluate as True if the diamonds list is empty. 
Inside this if statement's body, print the string "There are no more cards to pick."

 """

import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user_input = input("Press enter to pick a card, or Q then enter to quit: ")
    if user_input == "Q":
        break
    else:
       random_card = random.choice(diamonds)
       diamonds.remove(random_card)
       hand.append(random_card)
       print("Remaining cards: ", diamonds)
       print("Your hand: ", hand)

if not diamonds:
    print("There are no more cards to pick.")
    