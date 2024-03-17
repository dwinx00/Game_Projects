"""
  Program Description : Number Guess Game
  Language : Python 3
  Date Written : 10-27-2023
  Date Modified : 11-02-2023
  Programmers : Aldwin Guanzon
"""

import random


# Difficulty Menu Creation
def difficult_mode():
    while True:  # Main Menu
        try:
            print("--- Difficulty Options ---")
            print("  1 - Easy (10 Attempts) ")
            print("  2 - Medium (7 Attempts) ")
            print("  3 - Hard (5 Attempts) ")
            print("---------------------------")
            difficulty = int(input("Enter the Difficulty: "))
            assert difficulty in range(1, 4), "Invalid Input. Please Choose 1 to 3 Only"
            if difficulty == 1:
                return "Easy"

            elif difficulty == 2:
                return "Medium"

            elif difficulty == 3:
                return "Hard"

        except AssertionError as msg:
            print(msg)

        except ValueError:
            print("Invalid Input. Integers Only")


# Main Game
def numbergame():
    print("Welcome to Number Guess Game")
    print("You Will Guess the Random Number between 1 and 100")
    difficult_level = difficult_mode()
    print("The difficulty level is", difficult_level)
    # Easy Mode
    if difficult_level == "Easy":
        attempt = 10
        deduction = 50

    # Medium Mode
    elif difficult_level == "Medium":
        attempt = 7
        deduction = 75

    # Hard Mode
    elif difficult_level == "Hard":
        attempt = 5
        deduction = 100

    # Setting Game Parameters
    print(f"You have {attempt} Attempt And -{deduction} Points per Wrong Guess")
    user_attempt = 0
    user_score = 1000

    # Winning Number
    winning_number = random.randint(1, 100)

    # Hint Number
    hint_numb = random.randint(5, 10)

    # Game Loop
    while user_attempt < attempt:
        try:
            Guess_numb = int(input("Enter your Guess Number: "))
            if Guess_numb == winning_number:
                print(" You Guessed the Winning Number ")
                print(f" Your Final Score: {user_score}")
                break
            else:
                user_attempt += 1
                user_score -= deduction  # Deduct score points
                current_attempt = attempt - user_attempt
                print(f"The Remaining Attempt:{current_attempt}")
                print(f"The Current Score:{user_score}")
                # If Guess is Higher or Lower
                if Guess_numb > winning_number:
                    print(" The Guess is Too High")
                else:
                    print(" The Guess is Too Low")

            # Hint every two incorrect attempts
            if user_attempt % 2 == 0:
                hint = input("Do you Want Hint (Y/N): ")
                if hint.lower() == "y":
                    if winning_number < Guess_numb:
                        if winning_number - 10 < 1:  # if the hint number becomes negative or zero
                            print(f"The Winning Number is less than {Guess_numb} but greater than 1")
                        else:
                            print(
                                f"The Winning Number is less than {Guess_numb} but greater than {winning_number - hint_numb}")
                    else:
                        if winning_number + 10 > 100:  # if hint number will greater than 100
                            print(f"The Winning Number is greater than {Guess_numb} but less than 100")
                        else:
                            print(
                                f"The Winning Number is greater than {Guess_numb} but less than {winning_number + hint_numb}")
                else:
                    print("Good Luck!")

        except ValueError:
            print("Invalid Input. Integers Only")

    # Game Conclusion:
    else:
        print("You Lose")
    print(f"The Winning Number is {winning_number}")

    # Restart the Game
    restart = input(" Do You Want to Play Again (y/n): ")
    if restart.lower() == "y":
        numbergame()
    else:  # if not y then exit
        print("Thank You For Playing")


numbergame()
