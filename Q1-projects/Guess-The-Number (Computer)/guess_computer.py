import random

def guess_the_number():

    # Computer selects a random number between 1 and 100
    number = random.randint(1, 100)
    attempts = 0

    
    print("I've picked a number between 1 and 100.")
    
    print("Try to guess it!")
    
    while True:
        # Taking the user's guess
        guess = int(input("What's your guess? "))
        attempts += 1
        
        # Checking if the guess is correct
        if guess < number:
            print("Nope! My number is higher.")
        elif guess > number:
            print("Nope! My number is lower.")
        else:
            print(f"Congratulations! You found my number ({number}) in {attempts} attempts!")
            break

# Start the game
guess_the_number()