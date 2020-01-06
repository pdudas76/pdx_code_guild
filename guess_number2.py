# Import modules
import random

game_live = "yes"
game_count = 0
guess_count = 0
guess_correct = False
quit_current_game = 0

while game_live in ["yes", "y"]:
    computer_guess = random.randint(1, 10)
    while guess_count < 10 and guess_correct == 0:
            user_guess = input("\nGuess a number from 1 to 10: ")
            if user_guess.isdigit() and int(user_guess) in range(1,11):
                user_guess = int(user_guess)
                if user_guess == computer_guess:
                    guess_count += 1
                    print(f"You guessed correctly in {guess_count} tries.")
                    guess_correct = 1
                else:
                    if user_guess >= computer_guess:
                        print("\nYour guess was too high.")
                    else:
                        print("\nYour guess was too low.")
                    guess_count += 1
            else:
                print("\nYou did not enter a valid number.")
                quit_current_game = input("Do you want to quit? ")
                if quit_current_game in ["yes", "y"]:
                    print("")
                    guess_correct = 1
                else:
                    print("Let's try this again.")

    game_live = input("\nWould you like to play another game? ")
    guess_count = 0
    guess_correct = 0
    game_count += 1

if game_count == 0 or game_count > 1:
    print(f"\nYou played {game_count} games with the computer. Goodbye.\n")
else:
    print(f"\nYou played {game_count} game with the computer. Goodbye.\n")
