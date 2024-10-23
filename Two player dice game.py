import tkinter as tk
from tkinter import messagebox
import random

class DiceGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Two Player Dice Game")
        self.master.geometry("500x500")
        self.master.configure(bg="#282c34")
        
        self.player1_score = 0
        self.player2_score = 0

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.master, text="Two Player Dice Game", font=("Helvetica", 20, "bold"), bg="#282c34", fg="#61dafb")
        title_label.pack(pady=20)

        self.score_label = tk.Label(self.master, text=f"Player 1: {self.player1_score}  |  Player 2: {self.player2_score}", font=("Helvetica", 16), bg="#282c34", fg="#ffffff")
        self.score_label.pack(pady=10)

        self.player1_dice = tk.Label(self.master, text="", font=("Helvetica", 48), bg="#282c34", fg="#61dafb")
        self.player1_dice.pack(side="left", padx=20, pady=20)

        self.player2_dice = tk.Label(self.master, text="", font=("Helvetica", 48), bg="#282c34", fg="#61dafb")
        self.player2_dice.pack(side="right", padx=20, pady=20)

        roll_button = tk.Button(self.master, text="Roll Dice", command=self.roll_dice, bg="#61dafb", fg="#282c34", font=("Helvetica", 14), padx=10, bd=0)
        roll_button.pack(pady=20)

        self.result_label = tk.Label(self.master, text="", font=("Helvetica", 16), bg="#282c34", fg="#ffffff")
        self.result_label.pack(pady=10)

        restart_button = tk.Button(self.master, text="Restart Game", command=self.restart_game, bg="#ff6f61", fg="#ffffff", font=("Helvetica", 14), padx=10, bd=0)
        restart_button.pack(pady=20)

    def roll_dice(self):
        player1_roll = random.randint(1, 6)
        player2_roll = random.randint(1, 6)

        self.player1_score += player1_roll
        self.player2_score += player2_roll

        self.player1_dice.config(text=str(player1_roll))
        self.player2_dice.config(text=str(player2_roll))

        self.score_label.config(text=f"Player 1: {self.player1_score}  |  Player 2: {self.player2_score}")
        self.result_label.config(text=f"Player 1 rolled: {player1_roll}  |  Player 2 rolled: {player2_roll}")

        self.check_winner()

    def check_winner(self):
        if self.player1_score >= 30:
            messagebox.showinfo("Game Over", "Congratulations Player 1! You win!")
            self.restart_game()
        elif self.player2_score >= 30:
            messagebox.showinfo("Game Over", "Congratulations Player 2! You win!")
            self.restart_game()

    def restart_game(self):
        self.player1_score = 0
        self.player2_score = 0
        self.score_label.config(text=f"Player 1: {self.player1_score}  |  Player 2: {self.player2_score}")
        self.result_label.config(text="")
        self.player1_dice.config(text="")
        self.player2_dice.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = DiceGame(root)
    root.mainloop()

