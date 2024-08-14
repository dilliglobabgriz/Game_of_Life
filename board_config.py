import random
from typing import List

class Game_Board: 
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.board = [[]]

	def get_board(self):
		return self.board

	def get_dead_state(self) -> List[List[int]]:
		return [[0 for _ in range(self.columns)] for _ in range(self.rows)]

	def dead_state(self):
		self.board = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
		return

	def random_state(self):
		self.dead_state()
		for row in range(self.rows):
			for column in range(self.columns):
				self.board[row][column] = random.choice([0,1])	

	def set_board_state(self, grid: List[List[int]]):
		self.rows = len(grid)
		self.columns = len(grid[0])
		self.dead_state()

		for i in range(len(grid)):
			for j in range(len(grid[i])):
				self.board[i][j] = grid[i][j]

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
	
	def render_custom(self, board: List[List[int]]):
		rows = len(board)
		columns = len(board[0])
		print(' ' + '-' * (columns + 2) + ' ')
		for row in range(rows):
			print('| ', end='')
			for column in range(columns):
				print(self.get_cell_symbol(row, column), end='')
			print(' |')

	def get_cell_symbol(self, row, column):
		return '#' if self.board[row][column] else ' '


	def get_live_neighbors(self, row, column):
		live_neighbors = 0
		
		for i in range(row-1, row+2):
			for j in range(column-1, column+2):
				if (i >= 0) and (i < self.rows) and (j >= 0) and (j < self.columns) and (i != row or j != column):
					live_neighbors += self.board[i][j] 	
		#print(f'Cell ({row}, {column}): {live_neighbors} live neighbors')
		return live_neighbors	

	# Update each cell in the board to alive or dead based on rules of life
	def next_state(self):
		new_state = self.get_dead_state()
		for i in range(self.rows):
			for j in range(self.columns):
				new_state[i][j] = self.apply_rules_of_life(i, j)
				#self.render_custom(new_state)
		self.set_board_state(new_state)

	# Takes a cell as input and returns 0 or 1 based on Conway's Game of Life
	def apply_rules_of_life(self, row, column):
		live_neighbors = self.get_live_neighbors(row, column)
		status = 'alive' if self.board[row][column] == 1 else 'dead'		

		# Logic tree
		if status == 'dead':
			if live_neighbors == 3:     # Reproduction
				return 1
			return 0
		if live_neighbors > 3:               # Overpopulation
			return 0
		if live_neighbors >= 2:              # Goldylocks Zone
			return 1
		if live_neighbors >= 0:              # Underpopulation
			return 0
		else:				     # Error
			return -1                   

	
