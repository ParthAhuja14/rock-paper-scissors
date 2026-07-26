import random


def get_player_choice():
    """Prompt the user for rock, paper, scissors, or exit."""
    while True:
        player_choice = input("Enter rock, paper, scissors or exit: ").lower()
        if player_choice == "exit":
            print("Thanks for playing! Meet you next time!")
            exit()
        elif player_choice in ["rock", "paper", "scissors"]:
            return player_choice


def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(player_choice, computer_choice):
    """Determine the winner of a single round."""
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"


def play_round():
    """Play a single round and print the result."""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(player_choice, computer_choice))
    print("-" * 30)


def main():
    while True:
        play_round()


if __name__ == "__main__":
    main()
