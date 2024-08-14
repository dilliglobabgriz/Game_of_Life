from board_config import Game_Board
import time
from typing import List

grid1 = [
[0,0,0,0,0],
[0,0,1,0,0],
[0,0,1,0,0],
[0,0,1,0,0],
[0,0,0,0,0],
]

# Take a .txt file and convert it to a 2d grid
def load_board_state(file_path: str) -> List[List[int]]:
	grid = []
	txt_file = open(file_path, 'r')

	
	for line in txt_file:
		cur_line = []
		for char in line:
			if char == '0' or char == '1':
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
	board = Game_Board(40, 80)
	board.random_state()
	while True:
		board.render()
		board.next_state()
		time.sleep(.25)

def run_custom_game(file_path):
	board = Game_Board(0, 0)
	initial_state = load_board_state(file_path)
	board.set_board_state(initial_state)
	while True:
		board.render()
		board.next_state()
		time.sleep(.25)

def main():
	run_custom_game('starting_states/toad.txt')
	#run_big_game()

if __name__ == "__main__":
	main()
