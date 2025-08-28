import random
import time
from rich.console import Console
from rich.table import Table

# Game variables
score = 0
high_score = 0

console = Console()

def print_board(mole_row, mole_col):
    """Print the 3x3 game board with the mole position using rich styling"""
    table = Table(show_header=False, show_lines=True, border_style="bold red")  # <-- changed to red
    for _ in range(3):
        table.add_column(justify="center", style="bold")

    for row in range(3):
        cells = []
        for col in range(3):
            if row == mole_row and col == mole_col:
                cells.append("[bold green]O[/bold green]")
            else:
                cells.append("[dim].[/dim]")
        table.add_row(*cells)
    console.print("\n[bold yellow]--- WHACK-A-MOLE ---[/bold yellow]")
    console.print("[cyan]Use 'q' to quit at any time[/cyan]")
    console.print(table)

def move_mole():
    """Move the mole to a random position"""
    return random.randint(0, 2), random.randint(0, 2)

def get_player_input():
    """Get player's row and column input"""
    try:
        row_input = input("Enter row (0-2): ").strip()
        if row_input.lower() == 'q':
            return 'q', 'q'
        col_input = input("Enter column (0-2): ").strip()
        if col_input.lower() == 'q':
            return 'q', 'q'
            
        row = int(row_input)
        col = int(col_input)
        return row, col
    except ValueError:
        print("Please enter valid numbers!")
        return -1, -1

def play_game():
    """Main game function"""
    global score, high_score
    
    # Reset game variables
    score = 0
    mole_row, mole_col = move_mole()
    
    # Get player name
    player_name = input("Enter your name: ")
    print(f"\nWelcome {player_name}! Whack the mole by entering row and column numbers.")
    print("Game will last for 30 seconds!")
    
    # Record start time
    start_time = time.time()
    last_move_time = start_time
    
    # Main game loop
    while True:
        # Calculate remaining time
        elapsed_time = time.time() - start_time
        time_left = max(0, 30 - int(elapsed_time))
        
        # Check if time is up
        if time_left <= 0:
            break
            
        # Print the board and score
        print(f"\nScore: {score} | High Score: {high_score} | Time Left: {time_left}s")
        print_board(mole_row, mole_col)
        
        # Get player input
        print("Whack the mole! (Enter row and column)")
        row, col = get_player_input()
        
        # Check for quit
        if row == 'q' and col == 'q':
            print("Game quit by player.")
            return
            
        # Check if player hit the mole
        if row == mole_row and col == mole_col:
            score += 20
            print("WHACK! You hit the mole! +20 points")
            mole_row, mole_col = move_mole()  # Move mole to new position
        elif 0 <= row <= 2 and 0 <= col <= 2:
            print("Missed! The mole wasn't there.")
            # Move mole after a few seconds even if missed
            if time.time() - last_move_time > 2:
                mole_row, mole_col = move_mole()
                last_move_time = time.time()
        else:
            print("Invalid input. Please enter numbers between 0-2.")
        
        # Occasionally move the mole automatically
        if time.time() - last_move_time > 3:
            mole_row, mole_col = move_mole()
            last_move_time = time.time()
    
    # Game over
    print(f"\nScore: {score} | High Score: {high_score} | Time Left: {time_left}s")
    print_board(mole_row, mole_col)
    print("\n--- GAME OVER ---")
    print(f"Final Score: {score}")
    
    # Update high score
    if score > high_score:
        high_score = score
        print("New High Score! Congratulations!")
    
    # Ask to play again
    play_again = input("Play again? (y/n): ").lower().strip()
    if play_again == 'y':
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nGame interrupted. Thanks for playing!")
