import random

while True:
    list = ["rock", "paper", "scissors"]
    bot = random.choice(list)
    player = str(input(f"enter  {list}\n"))
    
    if bot == player:
        print("draw")
    
    elif player == "rock":
        if bot == "scissors":
            print("you win")
        elif bot == "paper":
            print("you lost")
               
    elif player == "paper":
        if bot == "scissors":
            print("you lost")
        elif bot == "rock":
            print("you win")
        
    elif player == "scissors":
        if bot == "paper":
            print("you lost")
        if bot == "rock":
            print("you win")    
    
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    
