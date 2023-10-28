import random

choice = ['rock', 'paper', 'scissor']
computerChoice = random.choice(choice);

# Adding user input
userChoice = input("Enter your choice: ")
user = userChoice.lower()

if user != 'rock' and user != 'paper' and user != 'scissor':
    print("Wrong Choice!")
    exit()

if user == computerChoice:
    print("Your choice = ", user)
    print("Computer's choice = ", computerChoice)
    print("Draw!")
else:
    if user == 'rock':
        if computerChoice == 'paper':
            print("Your choice = ", user)
            print("Computer's choice = ", computerChoice)
            print("You lose!")
        elif computerChoice == 'scissor':
            print("Your choice = ", user)
            print("Computer's choice = ", computerChoice)
            print("You win!")
    elif user == 'paper':
        if computerChoice == 'rock':
            print("Your choice = ", user)
            print("Computer's choice = ", computerChoice)
            print("You win!")
        elif computerChoice == 'scissor':
            print("Your choice = ", user)
            print("Computer's choice = ", computerChoice)
            print("You lose!")
    else:
        if computerChoice == 'paper':
            print("Your choice = ", user)
            print("Computer's choice = ", computerChoice)
            print("You win!")
        elif computerChoice == 'rock':
            print("Your choice = ", user)
            print("Computer's choice = ", computerChoice)
            print("You lose!")