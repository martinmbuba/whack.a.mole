from db import SessionLocal
from models.player import Player #table
from models.game import Game #table

import random
import time

game_tuple = ("Whack-A-Mole",)
print(game_tuple[0])

# creating or fetching player from db
def create_player(session, name):
    player = session.query(Player).filter_by(name=name).first() #Starts a query on the player table,filters ,fetches row that matches
    if not player: #equivalent of if no player found create one
        player = Player(name=name)
        session.add(player)
        session.commit()
    return player

def play_game(session, player):
    score = 0
    grid_size = 3
    time_limit = 15
    start_time = time.time()

    print(f"\nGame starts! You have {time_limit} seconds to whack the mole!")

    while time.time() - start_time < time_limit: #game works till the time limit
        mole_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
        
        for row in range(grid_size):
            row_line = ""
            for col in range(grid_size):
                if (row, col) == mole_position:
                    row_line += "[M]"
                else:
                    row_line += "[ ]"
            print(row_line)

        try:
            guess_row = int(input("Row (0-2): "))
            guess_col = int(input("Col (0-2): "))
        except ValueError:
            print("Please type a number!")
            continue

        if (guess_row, guess_col) == mole_position:
            print("Hit!")
            score += 1
        else:
            print("Miss!")

        time_left = time_limit - int(time.time() - start_time)
        print(f"Time left: {time_left}s\n")

    print(f"\nTime’s up! {player.name} got {score} points!")

    new_game = Game(player_id=player.id, board={"score": score})
    session.add(new_game)
    session.commit()

def main():
    session = SessionLocal()
    print(f"Welcome to {game_tuple[0]}")  # only game name now
    name = input("Enter your name: ")
    player = create_player(session, name)

    while True:
        play_game(session, player)
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break

    session.close()

if __name__ == "__main__":
    main()
