def main():
    print(" Welcome to Terminal Whack-a-Mole! ")
    player_name = input("Please enter your name: ")
    print(f"Hello, {player_name}! Get ready to play Whack-a-Mole! ")


if __name__ == "__main__":
    main()

import tkinter as tk
import random

root = tk.Tk()
root.title("Whack.a.Mole")

rows = 3
cols = 3

frame = tk.Frame(root)
frame.pack()

buttons = []
target_position = None

def whack(r, c):
    global target_position
    if (r, c) == target_position:
        buttons[r][c].config(bg="green")
    else:
        buttons[r][c].config(bg="red")

    root.after(500, show_target)

def show_target():
    global target_position
    for row in buttons:
        for btn in row:
            btn.config(bg="lightgray")

    r = random.randint(0, rows-1)
    c = random.randint(0, cols-1)
    target_position = (r, c)
    buttons[r][c].config(bg="yellow")


for r in range(rows):
    row_buttons = []
    for c in range(cols):
        btn = tk.Button(frame, text=f"{r},{c}", width=8, height=4,
                        command=lambda r=r, c=c: whack(r, c))
        btn.grid(row=r, column=c, padx=5, pady=5)
        row_buttons.append(btn)
    buttons.append(row_buttons)

show_target()

root.mainloop()
