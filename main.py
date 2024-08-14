from board_config import Game_Board

def display_board_testing():
	board = Game_Board(40, 50)
	#board.dead_state()
	#board.display_board()
	board.random_state()
	#board.display_board()
	board.render()

def next_state_test():
	board = Game_Board(3,3)
	board.random_state()
	board.render()
	print(board.get_live_neighbors(1, 1))

def main():
	next_state_test()

if __name__ == "__main__":
	main()
