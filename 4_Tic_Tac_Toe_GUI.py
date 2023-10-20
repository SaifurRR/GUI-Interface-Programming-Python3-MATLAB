"""
This code uses the 'tkinter' library to create a 3x3 squares Tic Tac Toe GUI for 2 users.
First player chooses "X" and second player chooses "0" and take turns until a straight
line (horizontal, vertical, diagonal) is drawn.

GUI Display: 
3x3 Tic Tac Toe Grid with "X" and "O" as user token. 
"""

import tkinter as tk
import numpy as np

# Constants
BOARD_SIZE = 600
SYMBOL_SIZE = (BOARD_SIZE / 3 - BOARD_SIZE / 8) / 2
SYMBOL_THICKNESS = 50
SYMBOL_X_COLOR = '#EE4035'
SYMBOL_O_COLOR = '#0492CF'
GREEN_COLOR = '#7BC043'

class TicTacToeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Tic-Tac-Toe')
        self.canvas = tk.Canvas(self.window, width=BOARD_SIZE, height=BOARD_SIZE)
        self.canvas.pack()
        self.window.bind('<Button-1>', self.handle_click)

        self.initialize_board()
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3, 3))

        self.player_X_starts = True
        self.reset_board = False
        self.game_over = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False

        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0

    def mainloop(self):
        self.window.mainloop()

    def initialize_board(self):
        # Create grid lines for the game board
        for i in range(2):
            self.canvas.create_line((i + 1) * BOARD_SIZE / 3, 0, (i + 1) * BOARD_SIZE / 3, BOARD_SIZE)
            self.canvas.create_line(0, (i + 1) * BOARD_SIZE / 3, BOARD_SIZE, (i + 1) * BOARD_SIZE / 3)

    def play_again(self):
        # Reset the game board for a new round
        self.initialize_board()
        self.player_X_starts = not self.player_X_starts
        self.player_X_turns = self.player_X_starts
        self.board_status = np.zeros(shape=(3, 3))

    def draw_O(self, logical_position):
        # Draw the "O" symbol on the canvas
        logical_position = np.array(logical_position)
        grid_position = self.logical_to_grid_position(logical_position)
        self.canvas.create_oval(grid_position[0] - SYMBOL_SIZE, grid_position[1] - SYMBOL_SIZE,
                                grid_position[0] + SYMBOL_SIZE, grid_position[1] + SYMBOL_SIZE, width=SYMBOL_THICKNESS,
                                outline=SYMBOL_O_COLOR)

    def draw_X(self, logical_position):
        # Draw the "X" symbol on the canvas
        grid_position = self.logical_to_grid_position(logical_position)
        self.canvas.create_line(grid_position[0] - SYMBOL_SIZE, grid_position[1] - SYMBOL_SIZE,
                                grid_position[0] + SYMBOL_SIZE, grid_position[1] + SYMBOL_SIZE, width=SYMBOL_THICKNESS,
                                fill=SYMBOL_X_COLOR)
        self.canvas.create_line(grid_position[0] - SYMBOL_SIZE, grid_position[1] + SYMBOL_SIZE,
                                grid_position[0] + SYMBOL_SIZE, grid_position[1] - SYMBOL_SIZE, width=SYMBOL_THICKNESS,
                                fill=SYMBOL_X_COLOR)

    def display_game_over(self):
        # Display game over message and scores
        if self.X_wins:
            self.X_score += 1
            text = 'Winner: Player 1 (X)'
            color = SYMBOL_X_COLOR
        elif self.O_wins:
            self.O_score += 1
            text = 'Winner: Player 2 (O)'
            color = SYMBOL_O_COLOR
        else:
            self.tie_score += 1
            text = 'It\'s a tie'
            color = 'gray'

        self.canvas.delete('all')
        self.canvas.create_text(BOARD_SIZE / 2, BOARD_SIZE / 3, font='cmr 60 bold', fill=color, text=text)
        score_text = 'Scores \n'
        self.canvas.create_text(BOARD_SIZE / 2, 5 * BOARD_SIZE / 8, font='cmr 40 bold', fill=GREEN_COLOR, text=score_text)
        score_text = 'Player 1 (X) : ' + str(self.X_score) + '\n'
        score_text += 'Player 2 (O): ' + str(self.O_score) + '\n'
        score_text += 'Tie                    : ' + str(self.tie_score)
        self.canvas.create_text(BOARD_SIZE / 2, 3 * BOARD_SIZE / 4, font='cmr 30 bold', fill=GREEN_COLOR, text=score_text)
        self.reset_board = True
        score_text = 'Click to play again \n'
        self.canvas.create_text(BOARD_SIZE / 2, 15 * BOARD_SIZE / 16, font='cmr 20 bold', fill='gray', text=score_text)

    def logical_to_grid_position(self, logical_position):
        # Convert logical grid position to pixel position
        logical_position = np.array(logical_position, dtype=int)
        return (BOARD_SIZE / 3) * logical_position + BOARD_SIZE / 6

    def grid_to_logical_position(self, grid_position):
        # Convert pixel position to logical grid position
        grid_position = np.array(grid_position)
        return np.array(grid_position // (BOARD_SIZE / 3), dtype=int)

    def is_grid_occupied(self, logical_position):
        # Check if a grid position is occupied
        if self.board_status[logical_position[0]][logical_position[1]] == 0:
            return False
        else:
            return True

    def is_winner(self, player):
        # Check if a player has won
        player = -1 if player == 'X' else 1
        for i in range(3):
            if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                return True
            if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                return True
        if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
            return True
        if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
            return True
        return False

    def is_tie(self):
        # Check if the game has resulted in a tie
        r, c = np.where(self.board_status == 0)
        tie = False
        if len(r) == 0:
            tie = True
        return tie

    def is_game_over(self):
        # Check if the game is over (either a win or a tie)
        self.X_wins = self.is_winner('X')
        if not self.X_wins:
            self.O_wins = self.is_winner('O')
        if not self.O_wins:
            self.tie = self.is_tie()
        return self.X_wins or self.O_wins or self.tie

    def handle_click(self, event):
        # Handle user clicks
        grid_position = [event.x, event.y]
        logical_position = self.grid_to_logical_position(grid_position)
        if not self.reset_board:
            if self.player_X_turns:
                if not self.is_grid_occupied(logical_position):
                    self.draw_X(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = -1
                    self.player_X_turns = not self.player_X_turns
            else:
                if not self.is_grid_occupied(logical_position):
                    self.draw_O(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = 1
                    self.player_X_turns = not self.player_X_turns
            if self.is_game_over():
                self.display_game_over()
        else:
            self.canvas.delete('all')
            self.play_again()
            self.reset_board = False

# Create an instance of the game and start the main loop
game_instance = TicTacToeGame()
game_instance.mainloop()
