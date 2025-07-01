import random

# Score tracking
user_score = 0
computer_score = 0

# Available choices
choices = ['rock', 'paper', 'scissors']

def get_user_choice():
    while True:
        user_input = input("Choose Rock, Paper, or Scissors: ").lower()
        if user_input in choices:
            return user_input
        print("Invalid choice! Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user, computer):
    global user_score, computer_score
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

def show_scores():
    print(f"\nScoreboard:\nYou: {user_score} | Computer: {computer_score}\n")

def play_game():
    print("=== Welcome to Rock, Paper, Scissors ===")
    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        determine_winner(user, computer)
        show_scores()

        again = input("Do you want to play again? (yes/no): ").lower()
        if again != 'yes':
            print("\nThanks for playing!")
            break

# Run the game
play_game()
