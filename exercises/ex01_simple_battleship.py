"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730387535"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
player1_boat_location: int = int(input("Pick a secret boat location between 1 and 4: "))
if player1_boat_location < 1: 
    print(f"Error! {player1_boat_location} too low!")
    exit()
if player1_boat_location > 4: 
    print(f"Error! {player1_boat_location} too high!")
    exit()
player2_guess: int = int(input("Guess a number between 1 and 4: "))
if player2_guess < 1: 
    print(f"Error! {player2_guess} too low!")
    exit()
if player2_guess > 4: 
    print(f"Error! {player2_guess} too high!")
    exit()
if player2_guess == player1_boat_location:
    if player2_guess == 1:
        print(f"{RED_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
    if player2_guess == 2:
        print(f"{BLUE_BOX}{RED_BOX}{BLUE_BOX}{BLUE_BOX}")
    if player2_guess == 3:
        print(f"{BLUE_BOX}{BLUE_BOX}{RED_BOX}{BLUE_BOX}")
    if player2_guess == 4:
        print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{WHITE_BOX}")
    print("Correct! You hit the ship.")
else: 
    if player2_guess == 1:
        print(f"{WHITE_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
    if player2_guess == 2:
        print(f"{BLUE_BOX}{WHITE_BOX}{BLUE_BOX}{BLUE_BOX}")
    if player2_guess == 3:
        print(f"{BLUE_BOX}{BLUE_BOX}{WHITE_BOX}{BLUE_BOX}")
    if player2_guess == 4:
        print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{WHITE_BOX}")
    print("Incorrect! You missed the ship.")
    