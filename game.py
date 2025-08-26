def main():
    print(" Welcome to Terminal Whack-a-Mole! ")
    player_name = input("Please enter your name: ")
    print(f"Hello, {player_name}! Get ready to play Whack-a-Mole! ")


if __name__ == "__main__":
    main()

import tkinter as tk

root = tk.Tk()
root.title("Whack.a.Mole")

rows = 3
cols = 3

frame = tk.Frame(root)
frame.pack()

buttons = []
for r in range(rows):
    row_buttons = []
    for c in range(cols):
        btn = tk.Button(frame, text=f"{r},{c}", width=8, height=4)
        btn.grid(row=r, column=c, padx=5, pady=5)
        row_buttons.append(btn)
    buttons.append(row_buttons)

root.mainloop()
