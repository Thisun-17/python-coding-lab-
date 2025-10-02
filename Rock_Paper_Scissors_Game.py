import random # Importing the random module to generate random choices for the computer

# Constants for choices 
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis ={ ROCK: '🪨', SCISSORS: '📄', SCISSORS: '✂️' } 
choices = tuple(emojis.keys()) 

def get_user_choice(): # Get user input and validate it
    while True:
        user_choice = input('Rock, Paper, or Scissors? (r/p/s): ').lower() 
        if user_choice in choices: 
            return user_choice
        else:
            print('Invalid choice! Please choose r, p, or s.')

def display_choices(user_choice, computer_choice): # Display choices 
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice): # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == PAPER and computer_choice == ROCK) or 
        (user_choice == SCISSORS and computer_choice == PAPER)):
        print("You win!")
    else:
        print("Computer wins!")

def play_game(): # Main game loop
    while True:
        user_choice = get_user_choice()
        
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice) 

        determine_winner(user_choice, computer_choice)

    
        should_continue = input('Do you want to play again? (y/n): ').lower()
        if should_continue == 'n':
            break

play_game() # Start the game 

