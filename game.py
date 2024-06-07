#!/usr/bin/pyhton3

<name:Winnie Mutheu email:mutheuw62@gmail.com>

 import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.board = [" "] * 9  # Initialize the board
        
        # Create buttons for each cell
        self.buttons = []
        for i in range(9):
            btn = tk.Button(self.root, text=" ", font=("Helvetica", 20), width=4, height=2,
                            command=lambda idx=i: self.make_move(idx))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def make_move(self, idx):
        if self.board[idx] == " ":
            self.board[idx] = "X"  # Assume player is X for simplicity
            self.buttons[idx].config(text="X")
            if self.check_winner("X"):
                messagebox.showinfo("Game Over", "Player X wins!")
                self.reset_board()
            # Add logic for computer's move or for two players
        else:
            messagebox.showwarning("Invalid Move", "This cell is already occupied!")
    
    def check_winner(self, player):
        # Implement winning logic here
        # Return True if the player wins, False otherwise
        pass

    def reset_board(self):
        self.board = [" "] * 9
        for btn in self.buttons:
            btn.config(text=" ")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
