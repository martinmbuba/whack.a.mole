import tkinter as tk

# Game values (dummy for now)
score = 0
high_score = 0
time_left = 30  # seconds

def main():
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
            btn = tk.Button(frame, text=f"{r},{c}", width=8, height=4)
            btn.grid(row=r, column=c, padx=5, pady=5)
            row_buttons.append(btn)
        buttons.append(row_buttons)

    root.mainloop()


if __name__ == "__main__":
    main()

