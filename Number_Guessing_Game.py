import random # Import the random module

number_to_guess = random.randint(1, 100) # Generate a random number between 1 and 100

# Ask the user to guess it 
while True:
    try:
        guess = int(input("Guess a number between 1 and 100: ")) 
        # Check if the guess is correct 
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed it!")
            break

    except ValueError:
        print("Please enter a valid integer.")
        # Handle invalid input







