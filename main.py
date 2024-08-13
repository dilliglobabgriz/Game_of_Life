from board_config import Game_Board

def display_board_testing():
	board = Game_Board(4, 6)
	board.dead_state()
	board.display_board()
	board.random_state()
	board.display_board()
	board.render()

def main():
	display_board_testing()

if __name__ == "__main__":
	main()
