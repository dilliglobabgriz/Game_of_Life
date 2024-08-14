from board_config import Game_Board
import time
from typing import List
import sys

grid1 = [
[0,0,0,0,0],
[0,0,1,0,0],
[0,0,1,0,0],
[0,0,1,0,0],
[0,0,0,0,0],
]

# Take a .txt file and convert it to a 2d grid
def get_board_state(file_path: str) -> List[List[int]]:
	grid = []
	valid_chars = ['0', '1']
	txt_file = open(file_path, 'r')

	for line in txt_file:
		cur_line = []
		for char in line:
			if char in valid_chars:
				cur_line.append(int(char))
		grid.append(cur_line)

	txt_file.close()

	return grid

def display_board_testing():
	board = Game_Board(40, 50)
	#board.dead_state()
	#board.display_board()
	board.random_state()
	#board.display_board()
	board.render()

def live_neighbor_test():
	board = Game_Board(3,3)
	board.random_state()
	board.render()
	print(board.get_live_neighbors(1, 1))

def next_step_test():
	board = Game_Board(30, 60)
	board.random_state()
	board.render()
	board.next_state()
	board.render()

def run_game():
	board = Game_Board(5, 5)
	board.set_board_state(grid1)
	while True:
		board.render()
		board.next_state()
	
def run_big_game():
	board = Game_Board(30, 60)
	board.random_state()
	while True:
		board.render()
		board.next_state()
		time.sleep(.1)

def run_custom_game(file_path, delay = 0.2):
	initial_state = get_board_state(file_path)
	board = Game_Board(0, 0)
	board.set_board_state(initial_state)
	while True:
		board.render()
		board.next_state()
		time.sleep(delay)

def main():
	# Handle command line args
	num_args = len(sys.argv)
	
	if num_args == 1:
		run_big_game()
	if num_args == 2:	
		run_custom_game(f'starting_states/{sys.argv[1]}.txt')
	if num_args == 3:
		run_custom_game(f'starting_states/{sys.argv[1]}.txt', float(sys.argv[2]))
		

if __name__ == "__main__":
	main()
