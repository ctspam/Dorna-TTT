import tkinter as tk
import random
import time

first_move_done = False  # Flag to track if Robot 1 has made the center move
second_move_done = False  # Flag to track if Robot 2 has made the corner move

def play_X(player):
    global first_move_done, second_move_done

    # First move: Robot 1 (X) always in the center
    if not first_move_done and player == "X":
        if buttons[1][1]["text"] == "":
            buttons[1][1]["text"] = "X"
            first_move_done = True
            # play_O("O")
            root.after(500, lambda: play_O("O"))  # Delay O's move by 500ms
            return

    # # Second move: Robot 2 (O) in a random corner
    # if first_move_done and not second_move_done and player == "O":
    #     corners = [(0,0), (0,2), (2,0), (2,2)]
    #     available_corners = [pos for pos in corners if buttons[pos[0]][pos[1]]["text"] == ""]
    #     if available_corners:
    #         r, c = random.choice(available_corners)
    #         buttons[r][c]["text"] = "O"
    #         second_move_done = True
    #         return

    # All other moves: fill the next empty spot
    for r in range(3):
        for c in range(3):
            if buttons[r][c]["text"] == "":
                buttons[r][c]["text"] = player
                # play_O("O")
                root.after(500, lambda: play_O("O"))  # Delay O's move by 500ms
                return  # Only one move per click

# Random Moves            
def play_O(player):
    # global first_move_done, second_move_done

    # # First move: Robot 1 (X) always in the center
    # if not first_move_done and player == "X":
    #     if buttons[1][1]["text"] == "":
    #         buttons[1][1]["text"] = "X"
    #         first_move_done = True
    #         return

    # Second move: Robot 2 (O) in a random corner
    # if first_move_done and not second_move_done and player == "O":
        # corners = [(0,0), (0,2), (2,0), (2,2)]
        # available_corners = [pos for pos in corners if buttons[pos[0]][pos[1]]["text"] == ""]
    # if player == "O":
    # time.sleep(0.5)
    available_moves = [(r, c) for r in range(3) for c in range(3) if buttons[r][c]["text"] == ""]

    if available_moves:
        r, c = random.choice(available_moves)
        buttons[r][c]["text"] = "O"
        # second_move_done = True
        return

    # # All other moves: fill the next empty spot
    # for r in range(3):
    #     for c in range(3):
    #         if buttons[r][c]["text"] == "":
    #             buttons[r][c]["text"] = player
    #             return  # Only one move per click

# ------ Game GUI ----
# Create window
root = tk.Tk()
root.title("TTT Algorithm")

# 3x3 Grid
buttons = [[None for _ in range(3)] for _ in range(3)]
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(root, text="", font=("Helvetica", 32), width=5, height=2)
        buttons[r][c].grid(row=r, column=c)

# Control buttons
x_button = tk.Button(root, text="Robot 1", font=("Helvetica", 16), command=lambda: play_X("X"))
x_button.grid(row=3, column=0)

o_button = tk.Button(root, text="Robot 2", font=("Helvetica", 16), command=lambda: play_O("O"))
o_button.grid(row=3, column=2)

# Spacer
tk.Label(root, text=" ").grid(row=3, column=1)

root.mainloop()
