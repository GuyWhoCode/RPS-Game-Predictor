import random
from sklearn import svm

input_data = []
output_data = []
player_choice_history = []
MODEL_TRAINING_THRESHOLD = 3


def computer_next_choice():
    if len(player_choice_history) > MODEL_TRAINING_THRESHOLD:
        svm_model = svm.SVC()
        svm_model.fit(input_data, output_data)
        next_move_prediction = svm_model.predict(
            [[player_choice_history[-2], player_choice_history[-1]]])[0]
    else:
        next_move_prediction = random.randint(1, 3)

    print("Predicting the human player's next choice: ", next_move_prediction)

    if next_move_prediction == 1:
        return 2
    elif next_move_prediction == 2:
        return 3

    # By default, return 1
    return 1


'''
Formats model training data based on player choice history in this format:
input_data = [[1, 2], [2, 3], [3, 1], [1, 3], [3, 2], [2, 1]]
output_data = [2, 3, 1, 3, 2, 1]
'''
def format_training_data(data):
    CHOICE_MINIMUM = 3

    if len(data) >= CHOICE_MINIMUM:
        input_data.append([data[-3], data[-2]])
        output_data.append(data[-1])


# Main game loop
while True:
    player_choice = int(
        input("Please make a choice (1: Rock, 2: Paper, 3: Scissors): "))
    computer_choice = computer_next_choice()
    print("Computer chose:", computer_choice)

    player_choice_history.append(player_choice)
    format_training_data(player_choice_history)

    # checking winner guard clause
    if player_choice == 1 and computer_choice == 2 \
            or player_choice == 2 and computer_choice == 3 \
            or player_choice == 3 and computer_choice == 1:
        print("You lose!")
        continue

    # checking loser guard clause
    elif player_choice == 2 and computer_choice == 1 \
            or player_choice == 3 and computer_choice == 2 \
            or player_choice == 1 and computer_choice == 3:
        print("You win!")
        continue

    # default case is a tie
    print("Tie!")
