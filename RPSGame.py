from random import randint

# variables for counting and taking lifes
# 3 LIVES FOR EACH AT THE BEGINNING
player_wins = 3
computer_wins = 3

# available weapons => sore this an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer pick one item at random
computer = choices[randint(0, 2)]

# show the commputer's choice in the terminal window
print ("Computer chooses: ", computer)
print("Computer wins", computer_wins)
print("Player wins", player_wins)

while player is False:
    print("Choose your weapon!\n")
    player = input("Rock, Paper or Scissors?\n")
    print("Player chooses:", player)

    # check to see if you picked the same thing
    if (player == computer):
        print("Tie! Live to shoot another day")
    # if each wins - plus one life to the score
    # if each loses - minus one life from the score
    elif player == "Rock":
        if computer == "Paper":
            print("You lose", computer, "covers", player)
            computer_wins += 1
            print("Computer lives left", computer_wins)
            player_wins -= 1
            print("Your lives left", player_wins)
        else:
            print("You win!", player, "smashes", computer)
            player_wins += 1
            print("Your lives left", player_wins)
            computer_wins -= 1
            print("Computer lives left", computer_wins)

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
            computer_wins += 1
            print("Computer lives left", computer_wins)
            player_wins -= 1
            print("Your lives left", player_wins)
        else:
            print("You win!", player, "covers", computer)
            player_wins += 1
            print("Your lives left", player_wins)
            computer_wins -= 1
            print("Computer lives left", computer_wins)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
            computer_wins += 1
            print("Computer lives left", computer_wins)
            player_wins -= 1
            print("Your lives left", player_wins)
        else:
            print("You win!", player, "cuts", computer)
            player_wins += 1
            print("Your lives left", player_wins)
            computer_wins -= 1
            print("Computer lives left", computer_wins)

    elif player == "Quit":
        exit()

    if player_wins == 0:
        print("Game is over! Computer won")
        exit()

    if computer_wins == 0:
        print("You WON!")
        exit()
player = False
computer = choices[randint(0, 2)]
