# chess.py
# simulate random chess games with selected games.
# find the best game opening to play, statistically.
# kind of like bitcoin mining, but for chess and trying to zero opponent instead of hash.

import chess, secrets, sys

def get_move(board):
	poss_moves = str(board.legal_moves)
#	for i in ['(', ')', '>', ',']:	exec(f"poss_moves = poss_moves.replace('{i}','')")
	poss_moves = poss_moves.replace('(','')
	poss_moves = poss_moves.replace(')','')
	poss_moves = poss_moves.replace('>','')
	poss_moves = poss_moves.replace(',','')
	possible_moves = poss_moves.split()[3:]
	return possible_moves[secrets.randbelow(len(possible_moves))]

def possible_moves(board):
	poss_moves = str(board.legal_moves)
#	for i in ['(', ')', '>', ',']:	exec(f"poss_moves = poss_moves.replace('{i}','')")
	poss_moves = poss_moves.replace('(','')
	poss_moves = poss_moves.replace(')','')
	poss_moves = poss_moves.replace('>','')
	poss_moves = poss_moves.replace(',','')
	possible_moves = poss_moves.split()[3:]
	return possible_moves

def play(moves_to_make):
	board = chess.Board()
	moves = 0
	moves_made = []
	while not board.is_game_over():
		if moves <= len(moves_to_make):
			moves += 2
			board.push_san(moves_to_make[(moves//2)-1])
			moves_made.append(moves_to_make[(moves//2)-1])
			move = get_move(board)
			board.push_san(move)
		else:
			move = get_move(board)
			board.push_san(move)
			moves_made.append(move)
			moves += 1
	return [moves_made, ["white_wins", bool((len(moves_made)+1)%2)], moves, board.is_checkmate()]

def checkmate(moves_to_make):
	checkmate = False
	game = []
	while not checkmate:
		game = play(moves_to_make)
		checkmate = game[3]
	return game

def test_move_series(moves_to_test):
	white_wins = 0
	rounds = 0
	while True:
		white_wins += int(checkmate(moves_to_test)[1][1])
		rounds += 1
		x = str(white_wins)+"/"+str(rounds)
		if (rounds % 10) == 0:	print(x)


if len(sys.argv) > 1:
	test_move_series(sys.argv[1:])
