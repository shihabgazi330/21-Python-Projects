import random

print("Welcome to the Number Guesser Game!")
score = 0
playing = (input("Do you want to play? (Yes/No): ").strip().lower() == "yes")
if not playing:
    print("Maybe next time!")
    exit()
else:
    print("Great! Let's start the game.")

number_to_guess = random.randint(0, 100) # generate a random number between 0 and 100 (inclusive)

txt = "\nI have selected a number between 0 and 100. Can you guess it?"

for _ in range(10):
    print(txt)

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 0 <= guess <= 100:
                break
            print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Please enter a valid integer.")
    
    if guess == number_to_guess:
        print("Correct! You've guessed the number!")
        number_to_guess = random.randint(0, 100) # generate a new number for the next round
        score += 1
        print(f"Your current score is: {score}/10")
        txt = "\nI have selected a new number between 0 and 100. Can you guess it?"
    elif guess < number_to_guess:
        print(f"Too low! Guess higher next time.")
    else:
        print(f"Too high! Guess lower next time.")

print(f"\nYour final score is: {score}/10")