import random

while True:
    r = random.randint(1, 100)
    print("Welcome to the Guessing Game!")
    print("Guess the number between 1 and 100.")
    c = 1
    while True:
        d = int(input("Guess: "))
        if r == d:
            print(f"Congratulations! You guessed the number in {c} guesses.")
            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                exit()
            else:
                break
        elif r < d:
            print("Too high! Guess lower.")
        elif r > d:
            print("Too low! Guess higher.")
        c += 1

	
