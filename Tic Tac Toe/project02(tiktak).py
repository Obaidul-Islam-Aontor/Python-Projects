import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = "X"
buttons = []

def check_winner():
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            reset_board()
            return

    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        reset_board()

def on_click(index):
    global current_player
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player
        check_winner()
        current_player = "O" if current_player == "X" else "X"

def reset_board():
    global current_player
    current_player = "X"
    for button in buttons:
        button["text"] = ""

for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command=lambda idx=len(buttons): on_click(idx))
        btn.grid(row=i, column=j)
        buttons.append(btn)

root.mainloop()
