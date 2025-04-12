import random

# List of words to choose from
words = ["python", "programming", "computer", "algorithm", "database", "network"]

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

# Main Hangman game function
def play_hangman():
    word = random.choice(words)  # Pick a random word
    guessed_letters = set()      # Keep track of guessed letters
    attempts = 6                 # Number of wrong guesses allowed
    hangman_stages = [
        "  ____  \n |    |  \n      |  \n      |  \n      |  \n      |  \n=========",
        "  ____  \n |    |  \n O    |  \n      |  \n      |  \n      |  \n=========",
        "  ____  \n |    |  \n O    |  \n |    |  \n      |  \n      |  \n=========",
        "  ____  \n |    |  \n O    |  \n/|    |  \n      |  \n      |  \n=========",
        "  ____  \n |    |  \n O    |  \n/|\\   |  \n      |  \n      |  \n=========",
        "  ____  \n |    |  \n O    |  \n/|\\   |  \n/     |  \n      |  \n=========",
        "  ____  \n |    |  \n O    |  \n/|\\   |  \n/ \\   |  \n      |  \n========="
    ]

    print("Welcome to Hangman!")
    print(hangman_stages[0])
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        # Check if the guess is in the word
        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")
        else:
            print("Good guess!")

        # Display current state
        current_word = display_word(word, guessed_letters)
        print(hangman_stages[6 - attempts])
        print(current_word)

        # Check win condition
        if "_" not in current_word:
            print("Congratulations! You won!")
            break

    if attempts == 0:
        print(f"Game Over! The word was: {word}")

# Start the game
if __name__ == "__main__":
    play_hangman()