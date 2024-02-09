import random 

def get_next_choice_for_computer():
  # update the latest human player choice records

  # re-train the model
  # just use SVM model

  # predict the next human player choice

  # choose the best next choice for computer, and return it
  return random.randint(1, 3)

while True:
  player_choice = int(input("Please make a choice (1: Rock, 2: Paper, 3: Scissors): "))
  computer_choice = get_next_choice_for_computer() # random.randint(1, 3) # improve the computer's strategy here
  print("Computer chose: ", computer_choice)
  
  if player_choice == 1 and computer_choice == 2 \
      or player_choice == 2 and computer_choice == 3 \
      or player_choice == 3 and computer_choice == 1:  
    print("You lose!")
  elif player_choice == 2 and computer_choice == 1 \
      or player_choice == 3 and computer_choice == 2 \
      or player_choice == 1 and computer_choice == 3:  
    print("You win!")
  else:
    print("Tie!")
  

