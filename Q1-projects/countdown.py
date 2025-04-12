import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Convert seconds into minutes and seconds
        timer = f'{mins:02d}:{secs:02d}'  # Format as MM:SS
        print(timer, end='\r')  # Print timer, overwrite previous line
        time.sleep(1)  # Wait 1 second
        seconds -= 1
    print("00:00 - Time's up!")

# Get input from the user
try:
    user_input = int(input("Enter the time in seconds: "))
    if user_input <= 0:
        print("Please enter a positive number of seconds.")
    else:
        countdown_timer(user_input)
except ValueError:
    print("Invalid input! Please enter a number.")