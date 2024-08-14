from board_config import Game_Board

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
	board = Game_Board(30, 60)
	
	while True:
		board.render()
		board.next_state()
	

def main():
	run_game()

if __name__ == "__main__":
	main()
