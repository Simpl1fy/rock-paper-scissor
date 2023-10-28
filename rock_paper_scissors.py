import random

def check_error(x):     #Function to fix error
    if x != 'rock' and x != 'paper' and x != 'scissor':
        return 1        #Returning 1 to check outside the function and exit the program, if this function return 1

def game(x, cc):        # Game functions
    if x == cc:
        print("Your choice = ", x)
        print("Computer's choice = ", cc)
        print("Draw!")
    else:
        if x == 'rock':
            if cc == 'paper':
                print("Your choice = ", x)
                print("Computer's choice = ", cc)
                print("You lose!")
            elif cc == 'scissor':
                print("Your choice = ", x)
                print("Computer's choice = ", cc)
                print("You win!")
        elif x == 'paper':
            if cc == 'rock':
                print("Your choice = ", x)
                print("Computer's choice = ", cc)
                print("You win!")
            elif cc == 'scissor':
                print("Your choice = ", x)
                print("Computer's choice = ", cc)
                print("You lose!")
        else:
            if cc == 'paper':
                print("Your choice = ", x)
                print("Computer's choice = ", cc)
                print("You win!")
            elif cc == 'rock':
                print("Your choice = ", x)
                print("Computer's choice = ", cc)
                print("You lose!")


choice = ['rock', 'paper', 'scissor']
computerChoice = random.choice(choice)      # Random string is generated from the list choice

userInput = input("Enter a choice: ")
userInput.lower()           # Taking user input and and converting to lower case

error = check_error(userInput)
if error == 1:
    print("Wrong Choice!")
    exit()          # Exiting the program if the error is 1

game(userInput, computerChoice) # calling the game functions
