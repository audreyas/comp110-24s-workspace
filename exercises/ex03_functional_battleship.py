"""EX03 - Functional Battleship."""

__author__ = "730387535"
import random 

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid_size: int, row_or_column: str) -> int:
    """Prompt and return the user's row or column guess."""
    assert row_or_column == "row" or row_or_column == "column"
    guess: int = int(input("Guess a " + row_or_column + ":" + " "))
    while int(guess) < 1 or int(guess) > grid_size:
        guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    if guess <= grid_size and guess > 0:
        return int(guess)
    return 0 


def print_grid(grid_size: int, row_guess: int, column_guess: int, user_guess: bool) -> None: 
    """Print a grid of boxes to represent the game board."""
    if user_guess is True:
        result_box: str = RED_BOX
    if user_guess is False:
        result_box = WHITE_BOX
    row_counter: int = 1
    while row_counter <= grid_size:
        singular_row: str = ""
        column_counter = 1
        if row_guess == row_counter:
            while column_counter <= grid_size:
                if column_guess == column_counter:
                    singular_row = singular_row + result_box
                else:
                    singular_row = singular_row + BLUE_BOX
                column_counter += 1
        else:
            while column_counter <= grid_size:
                singular_row = singular_row + BLUE_BOX
                column_counter += 1
        print(singular_row)
        row_counter += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:  
    """Given the secret boat location and the user's guess return if user was correct."""
    if secret_row == row_guess and secret_column == column_guess: 
        return True 
    else: 
        return False
    

def main(grid_size: int, secret_row: int, secret_column: int) -> None: 
    """Implement the main function.""" 
    turn_number: int = 1
    while turn_number < 6: 
        print(f"=== Turn {turn_number}/5 ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        corrguess = correct_guess(secret_row, secret_column, row_guess, column_guess)
        if corrguess is True:
            user_guess = True
            print_grid(grid_size, row_guess, column_guess, user_guess)
        else:
            user_guess = False
            print_grid(grid_size, row_guess, column_guess, user_guess)
        if corrguess is True:
            print("Hit!")
            print(f"You won in {turn_number}/5 turns!")
            turn_number = 7 
        else: 
            print("Miss!")
            turn_number += 1
        if turn_number == 6 and corrguess is False: 
            print("X/5 - Better luck next time!") 


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))