import tkinter as tk
import random

# Game values
score = 0
high_score = 0
time_left = 30  # seconds

# Global references
target_position = None
buttons = []
score_label = None
high_score_label = None
time_label = None
root = None

def main():
    global root, buttons, score_label, high_score_label, time_label, time_left

    print(" Welcome to Terminal Whack-a-Mole! ")
    player_name = input("Please enter your name: ")
    print(f"Hello, {player_name}! Get ready to play Whack-a-Mole! ")

    # Start GUI
    root = tk.Tk()
    root.title("Whack-a-Mole")

    # Info bar
    info_frame = tk.Frame(root)
    info_frame.pack(pady=10)

    tk.Label(info_frame, text=f"Player: {player_name}", font=("Arial", 12)).grid(row=0, column=0, padx=10)
    score_label = tk.Label(info_frame, text=f"Score: {score}", font=("Arial", 12))
    score_label.grid(row=0, column=1, padx=10)
    time_label = tk.Label(info_frame, text=f"Time Left: {time_left}s", font=("Arial", 12))
    time_label.grid(row=0, column=2, padx=10)
    high_score_label = tk.Label(info_frame, text=f"High Score: {high_score}", font=("Arial", 12))
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
        # Disable buttons
        for row in buttons:
            for btn in row:
                btn.config(state="disabled")

if __name__ == "__main__":
    main()
