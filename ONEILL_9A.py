#John O'Neill

# Create a rock-paper-scissors game!
# - Play once and report the result
# result =

#Pick one of rock, paper or scissors: rock
#Computer's choice: paper
#You lose!




# - Play in a loop and record how many wins and losses happen?
#10 Games: W's: 4, L's: 6, D's: 0



# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??





from numpy import random

class RPSGame:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def play_once(self, player1_choice, player2_choice):
        print(f"Player 1's choice: {player1_choice}")
        print(f"Player 2's choice: {player2_choice}")

        if player1_choice == player2_choice:
            print("It's a tie!")
            self.draws += 1
        elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
             (player1_choice == 'paper' and player2_choice == 'rock') or \
             (player1_choice == 'scissors' and player2_choice == 'paper'):
            print("Player 1 wins!")
            self.wins += 1
        else:
            print("Player 2 wins!")
            self.losses += 1

def play_game(num_players):
    game = RPSGame()
    while True:
        for _ in range(num_players):
            if num_players == 2:
                player1_choice = input("Player 1, pick rock, paper, or scissors: ")
                if player1_choice not in game.choices:
                    print("Invalid. Pick again.")
                    return
                player2_choice = input("Player 2, pick rock, paper, or scissors: ")
                if player2_choice not in game.choices:
                    print("Invalid. Pick again.")
                    return
                game.play_once(player1_choice, player2_choice)
            else:
                player1_choice = input("Player 1, pick rock, paper, or scissors: ")
                if player1_choice not in game.choices:
                    print("Invalid. Pick again.")
                    return
                computer_choice = random.choice(game.choices)
                print(f"Computer's choice: {computer_choice}")
                game.play_once(player1_choice, computer_choice)

        print(f"Wins: {game.wins}, Losses: {game.losses}, Draws: {game.draws}")

        play_again = input("Again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Bye, fool!")

def start_game():
    while True:
        num_players = int(input("Number of human players (0-2): "))
        if num_players < 0 or num_players > 2:
            print("Invalid number. Choose 0, 1, or 2.")
            continue
        play_game(num_players)

# Start the game
start_game()
