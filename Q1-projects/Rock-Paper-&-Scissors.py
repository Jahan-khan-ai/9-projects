import random

def play_game():
    # Options jo game mein honge
    choices = ["rock", "paper", "scissors"]
    
    # Computer randomly choose karega
    computer_choice = random.choice(choices)
    
    # User se input lenge
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    
    # Check karenge ki user ne valid choice enter ki hai
    while user_choice not in choices:
        print("Invalid choice! Please try again.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    
    # Dono choices ko print karenge
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")
    
    # Winner decide karne ke rules
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

# Game ko start karne ke liye
print("Welcome to Rock Paper Scissors!")
while True:
    play_game()
    # User se puchenge kya woh dobara khelna chahta hai
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break