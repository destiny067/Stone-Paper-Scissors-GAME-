import random

choices = ["STONE", "PAPER", "SCISSORS"]

print("Welcome to Stone Paper Scissors Game!")

while True:
    player = input("\nEnter Stone, Paper or Scissors: ").strip().upper()

    if player not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print(f"Computer chose: {computer}")
    if player == computer:
        print("It's a Draw!")

    elif player == "STONE" and computer == "SCISSORS":
        print("Stone breaks Scissors! You Win!")


    elif player == "PAPER" and computer == "STONE":
        print("Paper covers Stone! You Win!")

    elif player == "SCISSORS" and computer == "PAPER":
        print("Scissors cuts Paper! You Win!")


    else:
        print("Computer Wins!")
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()

    
    if again == "no":
        print("Thanks for playing!")
        break