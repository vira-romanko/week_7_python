from random import randint

player_lives = 5
computer_lives = 5

# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer pick one item at random
computer = choices[randint(0, 2)]


# define a win or lose function instead of the procedural way
def winorlose(status):
    # handle win or lose based on the status we pass in
    print("Called the win or lose function")
    print("***********************************")
    print("You", status, "!", "Would you like to play again?")
    choice = input("Y / N: ")

    if choice == "Y" or choice == "y":
        # reset the game
        # change global variables
        global player_lives
        global computer_lives
        global player
        global computer

        player_lives = 5
        computer_lives = 5
        player = False
        computer = choices[randint(0, 2)]

    elif choice == "N" or choice =="n":
        print("You chose to Quit")
        exit()

# show the computer choice in the terminal_window
# print("Computer chooses: ", computer)

while player is False:
    print("========================================")
    print("Player Lives:", player_lives, "/5")
    print("AI Lives:", computer_lives, "/5")
    print("========================================")
    print("Choose your weapon!\n")
    player = input("Rock, Paper or Scissors?\n")
    # print("Player chooses:", player)

    if player == "computer":
        print("Tie! Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
            player_lives -= 1
            print("You lose", computer, "covers", player, "\n")
        else:
            print("You win!", player, "smashes", computer, "\n")
            computer_lives -= 1

    elif player == "Paper":
        if computer == "Scissors":
            player_lives -= 1
            print("You lose!", computer, "cuts", player, "\n")
        else:
            print("You win!", player, "covers", computer, "\n")
            computer_lives -= 1

    elif player == "Scissors":
        if computer == "Rock":
            player_lives -= 1
            print("You lose!", computer, "smashes", player, "\n")
        else:
            print("You win!", player, "cuts", computer, "\n")
            computer_lives -= 1

    # handle win or lose
    if player_lives is 0:
        print("***************************")
        print("You lost! Would you like to play again?")
        choice = input("Y / N? ")
        print(choice)

        if choice == "Y" or choice == "y":
            # playing again, so reset lives etc
            player_lives = 5
            computer_lives = 5
            player = False
            computer = choices[randint(0, 2)]
        if choice == "n" or choice == "N":
            print("You Quit!")
            print("************************")
            exit()

    if computer_lives is 0:
        print("***************************")
        print("You won! Would you like to play again?")
        choice = input("Y / N? ")
        print(choice)

        if choice == "Y" or choice == "y":
            # playing again, so reset lives etc
            player_lives = 5
            computer_lives = 5
            player = False
            computer = choices[randint(0, 2)]
        if choice == "n" or choice == "N":
            print("You Quit!")
            print("************************")
            exit()

    player = False
    computer = choices[randint(0, 2)]
