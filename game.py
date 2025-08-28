import tkinter as tk
import random
import sql  # Import your database functions

# Game values
score = 0
high_score = 0
time_left = 30  # seconds
target_position = None
buttons = []
score_label = None
high_score_label = None
time_label = None
root = None
player_name = None


def main():
    global root, buttons, score_label, high_score_label, time_label, time_left, score, high_score, player_name

    sql.init_db()  # Initialize DB

    print(" Welcome to Terminal Whack-a-Mole! ")
    player_name = input("Please enter your name: ")

    player_data = sql.get_player(player_name)
    if player_data is None:
        sql.add_or_update_player(player_name, 0, 0)
        score, high_score = 0, 0
        print(f"Hello, {player_name}! Get ready to play Whack-a-Mole! ")
    else:
        score, high_score = player_data
        print(f"Welcome back, {player_name}! High Score: {high_score}")

    # Start GUI
    root = tk.Tk()
    root.title("Whack-a-Mole")

    # Info bar
    info_frame = tk.Frame(root)
    info_frame.pack(pady=10)

    tk.Label(info_frame, text=f"Player: {player_name}", font=(
        "Arial", 12)).grid(row=0, column=0, padx=10)
    score_label = tk.Label(
        info_frame, text=f"Score: {score}", font=("Arial", 12))
    score_label.grid(row=0, column=1, padx=10)
    time_label = tk.Label(
        info_frame, text=f"Time Left: {time_left}s", font=("Arial", 12))
    time_label.grid(row=0, column=2, padx=10)
    high_score_label = tk.Label(
        info_frame, text=f"High Score: {high_score}", font=("Arial", 12))
    high_score_label.grid(row=0, column=3, padx=10)

    # Game grid
    frame = tk.Frame(root)
    frame.pack(pady=20)

    rows, cols = 3, 3
    buttons.clear()
    for r in range(rows):
        row_buttons = []
        for c in range(cols):
            btn = tk.Button(frame, width=8, height=4, bg="lightgrey",
                            command=lambda r=r, c=c: whack(r, c))
            btn.grid(row=r, column=c, padx=5, pady=5)
            row_buttons.append(btn)
        buttons.append(row_buttons)

    countdown()
    move_mole()
    root.mainloop()


def move_mole():
    global target_position

    # Reset all buttons
    for r_idx, row in enumerate(buttons):
        for c_idx, btn in enumerate(row):
            btn.config(bg="lightgrey")

    # Select a new position
    r, c = random.randint(0, 2), random.randint(0, 2)
    target_position = (r, c)

    # Set the mole (green)
    buttons[r][c].config(bg="green")

    if time_left > 0:
        root.after(1000, move_mole)  # Move every second


def whack(r, c):
    global score, high_score

    if target_position == (r, c):
        score += 20
        score_label.config(text=f"Score: {score}")

        if score > high_score:
            high_score = score
            high_score_label.config(text=f"High Score: {high_score}")


def countdown():
    global time_left

    if time_left > 0:
        time_left -= 1
        time_label.config(text=f"Time Left: {time_left}s")
        root.after(1000, countdown)
    else:
        # Call game over when time is up
        game_over()
        # Disable buttons
        for row in buttons:
            for btn in row:
                btn.config(state="disabled")


def game_over():
    global score, time_left, high_score, player_name

    if score > high_score:
        high_score = score

    sql.add_or_update_player(player_name, score, high_score)

    # Disable buttons
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")

    # Show Game Over message and options
    game_over_label = tk.Label(root, text=f"Game Over! Your final score is: {score}", font=("Arial", 16))
    game_over_label.pack(pady=10)

    def restart():
        nonlocal game_over_label
        game_over_label.destroy()
        play_again_btn.destroy()
        quit_btn.destroy()

        restart_game()

    def quit_game():
        root.quit()

    play_again_btn = tk.Button(root, text="Play Again", command=restart)
    play_again_btn.pack()

    quit_btn = tk.Button(root, text="Quit", command=quit_game)
    quit_btn.pack()


def restart_game():
    global score, time_left, high_score, player_name

    score = 0
    time_left = 30

    sql.add_or_update_player(player_name, score, high_score)

    # Resetting the buttons
    for row in buttons:
        for btn in row:
            btn.config(state="normal", text="")

    # Update labels
    score_label.config(text=f"Score: {score}")
    time_label.config(text=f"Time Left: {time_left}s")
    high_score_label.config(text=f"High Score: {high_score}")

    # Restart game loop
    move_mole()
    countdown()


if __name__ == "__main__":
    main()


