""" 
Create a dice game.
 """

from hashlib import new
import random

high_score = 0
new_score = 0

while True:
    def dice_game():
        global high_score
        global new_score
        if new_score > high_score:
            high_score = new_score

        print(f"Current High Score: {high_score}")
        print("1) Roll Dice")
        print("2) Leave Game")
        player_choice = input("Enter your choice: ")
        while True:

            if player_choice == "1" or player_choice == "Roll Dice":
                die_roll_1 = random.randint(1, 6)
                die_roll_2 = random.randint(1, 6)
                print(f"\nYou roll a... {die_roll_1}")
                print(f"You roll a... {die_roll_2}")
                new_score = die_roll_1 + die_roll_2
                print(f"\nYou have rolled a total of: {new_score}\n")

                if  new_score > high_score:
                    print("New high score!\n")
                    break
                break
            elif player_choice == "2" or player_choice == "Leave Game":
                print("You have exited the game. Thanks for playing!")
                exit()


    dice_game()