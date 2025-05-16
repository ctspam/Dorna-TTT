import tkinter as tk
from tkinter import messagebox
import random

first_move_done = False
second_move_done = False
player_X_turn = True

def play_X(player):
    status_label.config(text="X's Turn", bg='orange')
    global first_move_done, second_move_done
    x_button.config(state="disabled")

    if not first_move_done:
        if buttons[1][1]["text"] == "":
            buttons[1][1]["text"] = "X"
            first_move_done = True
            if check_game_over():
                return
            root.after(500, lambda: play_O("O"))

            return

    else:
        for r in range(3):
            for c in range(3):
                if buttons[r][c]["text"] == "":
                    buttons[r][c]["text"] = player
                    if check_game_over():
                        return
                    root.after(500, lambda: play_O("O"))
                    o_button.config(state="normal")

                    return

def play_O(player):
    status_label.config(text="O's Turn", bg='red')
    available_moves = [(r, c) for r in range(3) for c in range(3) if buttons[r][c]["text"] == ""]
    o_button.config(state="disabled")

    if available_moves:
        r, c = random.choice(available_moves)
        buttons[r][c]["text"] = "O"
        if not check_game_over():
            x_button.config(state="normal")

def check_game_over():
    for i in range(3):
        if buttons[i][0]["text"] != "" and buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"]:
            end_game(f"Player {buttons[i][0]['text']} wins!")
            return True
        if buttons[0][i]["text"] != "" and buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"]:
            end_game(f"Player {buttons[0][i]['text']} wins!")
            return True

    if buttons[0][0]["text"] != "" and buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"]:
        end_game(f"Player {buttons[0][0]['text']} wins!")
        return True
    if buttons[0][2]["text"] != "" and buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"]:
        end_game(f"Player {buttons[0][2]['text']} wins!")
        return True

    if all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
        end_game("It's a draw!")
        return True

    return False

def end_game(message):
    messagebox.showinfo("Game Over", message)
    status_label.config(text="Game Over", bg='yellow')
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(state="disabled")
    x_button.config(state="disabled")
    o_button.config(state="disabled")

# ---- GUI Setup ----
root = tk.Tk()
root.title("TTT Algorithm")

# Status label (single instance!)
status_label = tk.Label(root, text="Welcome to Tic Tac Toe", bg='lightgreen', font=("Helvetica", 14))
status_label.grid(row=0, column=0, columnspan=3, pady=(10, 2))

# Game grid (3x3)
buttons = [[None for _ in range(3)] for _ in range(3)]
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(root, text="", font=("Helvetica", 32), width=5, height=2)
        buttons[r][c].grid(row=r + 1, column=c)

# Control buttons
x_button = tk.Button(root, text="Robot 1", font=("Helvetica", 16), command=lambda: play_X("X"))
x_button.grid(row=4, column=0)

tk.Label(root, text=" ").grid(row=4, column=1)  # spacer

o_button = tk.Button(root, text="Robot 2", font=("Helvetica", 16), command=lambda: play_O("O"))
o_button.grid(row=4, column=2)
# o_button.config(state="disabled")

root.mainloop()
