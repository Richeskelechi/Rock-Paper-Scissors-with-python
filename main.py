import random
# Here I am declaring a bool keep_running = True this will be used to keep the game running
keep_running = True
# Here I am creating a list of the possible choices
list_of_choices = ['r', 'p', 's']
# Here I am creating a dictionary that has the choices as the keys and the definition of the choices as the values
choice_definition = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors'
}
# I am creating a function for the play_game


def play_game():
    # The keep_running varaible I am making it global so that it can be used in the main function and the sun functions
    global keep_running
    # simple message that tells the player what the game is about
    print("Welcome to the game of Rock, Paper And Scissors!")
    print("The rules are simple: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
    print("Good luck!")
    # Here I am asking the user to choose either rock, paper, or scissors and I am storing the input in the user player variable
    user = input("Please enter your choice either 'r' or 'p' or 's': ")
    # Here I am converting the user input to lower case so that it can be compared to the opponent
    user = user.lower()
    # Here I am creating a list of the possible choices and using the random module to choose a random choice from the list and storing it in the computer variable
    computer = random.choice(list_of_choices)
    # Here I am checking to see if the user input is valid that is if it is one of the three choices
    if user in list_of_choices:
        # Here I am checking to see if the user input is the same as the computer input
        if user == computer:
            # Here I am printing a message that tells the user that he chose the same thing as the computer so its a tie so the game will run again because of the keep_running variable
            return (f"You Have Chosen ({choice_definition[user]}) And The Computer Have Chosen ({choice_definition[computer]}) So It's a tie!\nTry Again!")

        # Here I am checking for a winner so I am calling the is_win function and passing the user and computer variables as arguments
        if is_win(user, computer):
            # Here I am printing a message that tells the user that he has won the game so the game will end because of the keep_running variable is set to false
            keep_running = False
            return (f"You Have Chosen ({choice_definition[user]}) And The Computer Have Chosen ({choice_definition[computer]}) So You Win")
        # Here I am printing a message that tells the user that he has Lost the game so the game will end because of the keep_running variable is set to false
        keep_running = False
        return (f"You Have Chosen ({choice_definition[user]}) And The Computer Have Chosen ({choice_definition[computer]}) So You Lose")
    else:
        # Here I am printing a message that tells the user that the input is not valid so the game will start again because of the keep_running variable true
        return ("Invalid Input! Enter Only 'r' or 'p' or 's'")

# Here I Have My Function To Check For A Winner in the play_game()


def is_win(player, opponent):
    # Here I am checking to see if the player is rock and the opponent is scissors
    if player == 'r' and opponent == 's':
        return True
    # Here I am checking to see if the player is scissors and the opponent is paper
    elif player == 's' and opponent == 'p':
        return True
    # Here I am checking to see if the player is paper and the opponent is rock
    elif player == 'p' and opponent == 'r':
        return True
    # Here I am returning false if none of the above conditions are met
    else:
        return False


# Here I Have My while loop that will keep the game running as long as their Is A Tie between The User And The Computer
while keep_running:
    # Here I am calling the play_game function.
    print(play_game())
