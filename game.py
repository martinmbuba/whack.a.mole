import tkinter as tk
import random

# Game values (dummy for now)
score = 0
high_score = 0
time_left = 30  # seconds
target_position = None
buttons = []
score_label = None

def main():
    global root, buttons, score_label

    print(" Welcome to Terminal Whack-a-Mole! ")
    player_name = input("Please enter your name: ")
    print(f"Hello, {player_name}! Get ready to play Whack-a-Mole! ")

    # Start GUI
    root = tk.Tk()
    root.title("Whack-a-Mole")

    # Top info frame (Player name, Score, Time, High Score)
    info_frame = tk.Frame(root)
    info_frame.pack(pady=10)

    name_label = tk.Label(info_frame, text=f"Player: {player_name}", font=("Arial", 12))
    name_label.grid(row=0, column=0, padx=10)

    score_label = tk.Label(info_frame, text=f"Score: {score}", font=("Arial", 12))
    score_label.grid(row=0, column=1, padx=10)

    time_label = tk.Label(info_frame, text=f"Time Left: {time_left}s", font=("Arial", 12))
    time_label.grid(row=0, column=2, padx=10)

    high_score_label = tk.Label(info_frame, text=f"High Score: {high_score}", font=("Arial", 12))
    high_score_label.grid(row=0, column=3, padx=10)

    # Grid of buttons
    frame = tk.Frame(root)
    frame.pack(pady=20)

    rows = 3
    cols = 3
    buttons = []
    for r in range(rows):
        row_buttons = []
        for c in range(cols):
            btn = tk.Button(frame, text=f"{r},{c}", width=8, height=4,
                            command=lambda r=r, c=c: whack(r, c))
            btn.grid(row=r, column=c, padx=5, pady=5)
            row_buttons.append(btn)
        buttons.append(row_buttons)

    spawn_target()

    root.mainloop()

def spawn_target(exclude=None):
    global target_position, buttons
    for r_idx, row in enumerate(buttons):
        for c_idx, btn in enumerate(row):
            if exclude != (r_idx, c_idx):
                btn.config(bg="lightgrey")

    r, c = random.randint(0, 2), random.randint(0, 2)
    target_position = (r, c)
    buttons[r][c].config(bg="yellow")

def whack(r, c):
    global score, buttons, target_position, score_label

    if target_position == (r, c):
        buttons[r][c].config(bg="green")
        score += 1
    else:
        buttons[r][c].config(bg="red")

    spawn_target(exclude=(r, c))

    score_label.config(text=f"Score: {score}")

if __name__ == "__main__":
    main()
