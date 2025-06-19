import tkinter as tk
from tkinter import messagebox
from .board import Board
from .ai import AI
import pygame
import os

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe AI (Unbeatable)")
        self.window.configure(bg="white")
        self.window.minsize(400, 500)
        self.window.geometry("500x600")

        pygame.init()
        pygame.mixer.init()

        self.board = Board()
        self.ai = AI()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.stats = {
            "wins": 0,
            "losses": 0,
            "draws": 0
        }

        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        self.frame = tk.Frame(self.window, bg="white")
        self.frame.pack(pady=20)

        for r in range(3):
            for c in range(3):
                button = tk.Button(
                    self.frame,
                    text='',
                    font=('Helvetica', 32, 'bold'),
                    width=5,
                    height=2,
                    bg='white',
                    fg='black',
                    disabledforeground='black',
                    relief='ridge',
                    bd=3,
                    command=lambda row=r, col=c: self.human_move(row, col)
                )
                button.grid(row=r, column=c, padx=5, pady=5)
                self.buttons[r][c] = button

        self.restart_button = tk.Button(
            self.window,
            text="Restart",
            font=('Arial', 14, 'bold'),
            command=self.reset_game,
            bg="black",
            fg="white",
            activebackground="gray20",
            activeforeground="white",
            width=12,
            height=2,
            relief='raised',
            bd=3
        )
        self.restart_button.pack(pady=(10, 10))

        self.stats_label = tk.Label(
            self.window,
            text=self.get_stats_text(),
            font=('Arial', 14),
            bg='white',
            fg='black'
        )
        self.stats_label.pack(pady=(0, 10))

    def get_stats_text(self):
        total = self.stats['wins'] + self.stats['losses'] + self.stats['draws']
        return f"Matches: {total}  |  Wins: {self.stats['wins']}  |  Losses: {self.stats['losses']}  |  Draws: {self.stats['draws']}"

    def update_stats_label(self):
        self.stats_label.config(text=self.get_stats_text())

    def human_move(self, row, col):
        if self.board.make_move(row, col, 'X'):
            self.update_button(row, col, 'X')
            self.play_sound('click')
            if self.check_game_end('X'):
                return
            self.window.after(300, self.ai_move)

    def ai_move(self):
        row, col = self.ai.get_best_move(self.board)
        if self.board.make_move(row, col, 'O'):
            self.update_button(row, col, 'O')
            self.play_sound('click')
            self.check_game_end('O')

    def update_button(self, row, col, player):
        self.buttons[row][col].config(
            text=player,
            state='disabled',
            disabledforeground='black'
        )

    def check_game_end(self, player):
        if self.board.current_winner == player:
            self.highlight_winner(player)
            if player == 'X':
                self.stats['wins'] += 1
                self.play_sound('win')
            else:
                self.stats['losses'] += 1
                self.play_sound('lost')
            messagebox.showinfo("Game Over", f"{player} wins!")
            self.disable_all_buttons()
            self.update_stats_label()
            return True
        elif self.board.is_draw():
            self.stats['draws'] += 1
            self.play_sound('draw')
            messagebox.showinfo("Game Over", "It's a draw!")
            self.disable_all_buttons()
            self.update_stats_label()
            return True
        return False

    def disable_all_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state='disabled')

    def reset_game(self):
        self.board.reset()
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(
                    text='',
                    state='normal',
                    bg='white'
                )

    def highlight_winner(self, player):
        for r in range(3):
            if all(self.board.grid[r][c] == player for c in range(3)):
                for c in range(3):
                    self.buttons[r][c].config(bg='lightgreen')
                return
        for c in range(3):
            if all(self.board.grid[r][c] == player for r in range(3)):
                for r in range(3):
                    self.buttons[r][c].config(bg='lightgreen')
                return
        if all(self.board.grid[i][i] == player for i in range(3)):
            for i in range(3):
                self.buttons[i][i].config(bg='lightgreen')
            return
        if all(self.board.grid[i][2 - i] == player for i in range(3)):
            for i in range(3):
                self.buttons[i][2 - i].config(bg='lightgreen')
            return

    def play_sound(self, event):
        try:
            base_path = os.path.join(os.path.dirname(__file__), '../assets')
            sounds = {
                'click': 'click.mp3',
                'win': 'win.mp3',
                'lost': 'lost.mp3',
                'draw': 'draw.mp3'
            }
            path = os.path.join(base_path, sounds[event])
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
        except Exception as e:
            print("Sound error:", e)
 