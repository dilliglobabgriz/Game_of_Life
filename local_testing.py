from board_config import Game_Board

def test_dead_state():
	expected = [[0,0,0],[0,0,0],[0,0,0]]
	board = Game_Board(3, 3)
	board.dead_state()
	if board.get_board() == expected:
		print('dead_state functioning properly')
	else:
		print('FAIL: dead state did not give expected output')

def test_set_state():
	expected = [[1,0,0],[0,1,0],[0,0,1]]
	board = Game_Board(3, 3)
	board.set_board_state(expected)
	if board.get_board() == expected:
		print('set_board_state functioning properly')
	else:
		print('FAIL: set state did not give expected output')
	
def test_next_state():
	start_state = [[1,0,0],[0,1,0],[0,0,1]]
	expected = [[0,0,0],[0,1,0],[0,0,0]]
	board = Game_Board(3, 3)
	board.set_board_state(start_state)
	board.render()
	print(f'Center cell live neighbors: {board.get_live_neighbors(1, 1)}')
	board.next_state()
	if board.get_board() == expected:
		print('next_state simple test passed')
	else:
		print('FAIL: next_state')
		board.render()


def main():
	test_dead_state()
	test_set_state()
	test_next_state()

if __name__ == '__main__':
	main()
