"""EX02 - One Shot Battleship"""

__author__ = "730387535"

GRID_SIZE: int = 4
SECRET_ROW: int = 3
SECRET_COLUMN: int = 2

row_guess: int = int(input("Guess a row: "))
if row_guess == SECRET_ROW: 
    column_guess: int = int(input("Guess a column: "))
    if column_guess == SECRET_COLUMN:
        print("Hit!") 
        exit()
while row_guess >= GRID_SIZE: 
    if row_guess > GRID_SIZE:
        row_guess = int(input((f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: ")))
if row_guess <= GRID_SIZE:
    column_guess: int = int(input("Guess a column: "))
    if column_guess == SECRET_COLUMN:
        print("Hit!")
        exit()
while column_guess >= GRID_SIZE:
    if column_guess > GRID_SIZE: 
        coulmn_guess = int(input((f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: ")))
    if row_guess == SECRET_ROW: 
        if column_guess == SECRET_COLUMN:
        print("Hit!")
        exit()
if row_guess != SECRET_ROW:
    print("Miss!")4
    
    exit()







