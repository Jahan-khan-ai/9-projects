import random

def guess_the_number_user():
    print("Think of a number between 1 and 100, and I (the computer) will try to guess it!")
    print("After each guess, tell me: 'higher' (h), 'lower' (l), or 'correct' (c).")
    
    low = 1
    high = 100
    attempts = 0
    
    while True:
        # Computer makes a guess
        guess = random.randint(low, high)
        attempts += 1
        print(f"My guess is: {guess}")
        
        # User provides feedback
        feedback = input("Is it higher (h), lower (l), or correct (c)? ").lower()
        
        if feedback == 'h':
            low = guess + 1  # Adjust the lower bound
        elif feedback == 'l':
            high = guess - 1  # Adjust the upper bound
        elif feedback == 'c':
            print(f"I got it! Your number is {guess}, and it took me {attempts} attempts!")
            break
        else:
            print("Please enter 'h', 'l', or 'c' only.")
        
        if low > high:
            print("Something's wrong! I can't find a number. Did you give consistent feedback?")
            break

# Start the game
guess_the_number_user()