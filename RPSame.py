from random import randint

# available weapons => sore this an array
choices = ["Rock", "Paper", "Scissors"]

#make the computer pick one item at random
computer_choice = choices [randint(0,2)]
# show the commputer's choice in the terminal window
print ("Computer chooses: ", computer_choice)

