import random
from typing import List

class Game_Board: 
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.board = [[]]

	def dead_state(self):
		self.board = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
		return

	def random_state(self):
		self.dead_state()
		for row in range(self.rows):
			for column in range(self.columns):
				self.board[row][column] = random.choice([0,1])	

	def display_board(self):
		print(self.board)
		return

	def render(self):
		print(' ' + '-' * (self.columns + 2) + ' ')
		for row in range(self.rows):
			print('| ', end='')
			for column in range(self.columns):
				print(self.get_cell_symbol(row, column), end='')
			print(' |')
		print(' ' + '-' * (self.columns + 2) + ' ')

	def get_cell_symbol(self, row, column):
		return '#' if self.board[row][column] else '*'


	def get_live_neighbors(self, row, column):
		live_neighbors = 0
		
		for i in range(row-1, row+2):
			for j in range(column-1, column+2):
				if (i >= 0) and (i < self.rows) and (j >= 0) and (j < self.columns) and (i != row or j != column):
					live_neighbors += self.board[i][j] 	

		return live_neighbors	

	def next_state(self):
		pass
