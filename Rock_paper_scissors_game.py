import random
# This is matrix that will determine who will be the winner in the game
Game_matrix = [
    [0, -1, 1],
    [1, 0, -1],
    [-1, 1, 0]
]
# Match the user input with the game matrix
def determine_winner(choice1, choice2):
    result = Game_matrix[choice1][choice2]
    if result == 1:
        return "Player 1 wins!"
    elif result == -1:
        return "Player 2 wins!"
    else:
        return "It's a tie!"
# Show the rules of the game.
def display_game_rules():
    print("""
Rock-Paper-Scissors Rules:
- The game is played between two players, typically you (the user) and the computer.
- Each player selects one of three options: rock, paper, or scissors.
- The winner is determined by the following rules:
  - Rock crushes scissors.
  - Scissors cuts paper.
  - Paper covers rock.
- If both players choose the same option, the game is a tie.
- You can play as many rounds as you like!
""")
#display the 1st player choice
def display_1st_player_choice(player1_choice):
    if player1_choice == 0:
        print("The first player choice : Rock ")
    elif player1_choice == 1:
        print("The first player choice : Paper ")
    else:
        print("The first player choice : Scissors ")

# Display the 2nd player choice
def display_2nd_player_choice(player2_choice):
    if player2_choice == 0:
        print("The 2nd player choice : Rock ")
    elif player2_choice == 1:
        print("The 2nd player choice : Paper ")
    else:
        print("The 2nd player choice : Scissors ")

# The main funtion
def main():
    print("*-----Welcome to Rock, Paper-----*")
    print("1. Play with another player.")
    print("2. Play with the computer.")
    print("3. Rules of the game.")
    print("4. Exit")
    answer = int(input("Enter your choice(1/2/3/4): "))

    if answer == 1:
        player1_choice = int(input("Player 1: "))
        player2_choice = int(input("Player 2: "))
        display_1st_player_choice(player1_choice)
        display_2nd_player_choice(player2_choice)
        print(determine_winner(player1_choice, player2_choice))
        main()
    elif answer == 2:
        player_choice = int(input("Your choice (0 for rock, 1 for paper, 2 for scissors): "))
        computer_choice = random.randint(0, 2)  # computer choice a random number between (0,1,2)
        display_1st_player_choice(player_choice)
        display_2nd_player_choice(computer_choice)
        print(determine_winner(player_choice, computer_choice))
        main()
    elif answer == 3:
        display_game_rules()
        main()
    elif answer == 4:
        print("Thanks for playing!")
    else:
        print("Invalid input. Please enter 1, 2, 3, or 4.")
        main()

# Running the game
if __name__ == '__main__':
    main()