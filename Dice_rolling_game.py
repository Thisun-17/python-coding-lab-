import random # Import the random module 

while True: 
# Ask: roll the dice?
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y': 
        die1 = random.randint(1, 6) 
        die2 = random.randint(1, 6)
        print(f'You rolled a {die1} and a {die2}.') 
    elif choice == 'n': 
        print('Thank you for playing.') 
        break 
    else: 
        print('Invalid input. Please enter y or n.') 
        continue


 
