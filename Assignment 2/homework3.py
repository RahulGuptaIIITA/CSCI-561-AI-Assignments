board_values = list()
you_play = ' '
op_play = ' '
cutoff_depth = 0
n = 0

def resulting_state(current_board_state, n, row, col, current_player, op_player, move):
	next_board_state = [[' ' for i in range(n)] for j in range(n)]
	flag = 0
		
	for i in range(n):
		for j in range(n):
			next_board_state[i][j] = current_board_state[i][j]

	if move=='Stake':
		next_board_state[row][col] = current_player
		#print("Stake by " + current_player + " " + str(next_board_state))
	elif move=='Raid':
		next_board_state[row][col] = current_player
		if (row+1)<n:
			if next_board_state[row+1][col]==op_player:
				next_board_state[row+1][col] = current_player
				flag = 1
		if (row-1)>=0:
			if next_board_state[row-1][col]==op_player:
				next_board_state[row-1][col] = current_player
				flag = 1
		if (col+1)<n:
			if next_board_state[row][col+1]==op_player:
				next_board_state[row][col+1] = current_player
				flag = 1
		if (col-1)>=0:
			if next_board_state[row][col-1]==op_player:
				next_board_state[row][col-1] = current_player
				flag = 1
		#print("Raid by " + current_player + " " + str(next_board_state))
	return tuple((next_board_state, flag))

def calc_gamescore(state):
	score = 0
	for i in range(n):
		for j in range(n):
			if state[i][j]==you_play:
				score += board_values[i][j]
			elif state[i][j]==op_play:
				score -= board_values[i][j]
	return score

def minimax_min(current_state, n, current_player, op_player, depth):
	if depth==cutoff_depth:
		return tuple((calc_gamescore(current_state), None, None, None))

	gamescore = float('infinity')
	my_next_move = None
	temp_next_state = None
	free_spots_present = 0

	for i in range(n):
		for j in range(n):
			if current_state[i][j]=='.':
				if free_spots_present==0:
					free_spots_present = 1
				temp_next_state = resulting_state(current_state, n, i, j, current_player, op_player, 'Stake')
				temp = min(gamescore, minimax_max(temp_next_state[0], n, op_player, current_player, depth+1)[0])
				if temp!=gamescore:
					gamescore = temp
					my_next_move = temp_next_state[0]
					action = 'Stake'
					move = str(chr(65+j)) + str(i+1)

	if free_spots_present==0:
		return tuple((calc_gamescore(current_state), None, None, None))

	for i in range(n):
		for j in range(n):
			flag = 0
			if current_state[i][j]=='.':
				
				if (i+1)<n:
					if current_state[i+1][j]==current_player:
						flag = 1
				if (i-1)>=0:
					if current_state[i-1][j]==current_player:
						flag =  1
				if (j+1)<n:
					if current_state[i][j+1]==current_player:
						flag = 1
				if (j-1)<n:
					if current_state[i][j-1]==current_player:
						flag = 1

				if flag==1:
					temp_next_state = resulting_state(current_state, n, i, j, current_player, op_player, 'Raid')
					temp = min(gamescore, minimax_max(temp_next_state[0], n, op_player, current_player, depth+1)[0])
					if temp!=gamescore:
						gamescore = temp
						my_next_move = temp_next_state[0]
						if temp_next_state[1]==1:
							action = 'Raid'
						else:
							action = 'Stake'
						move = str(chr(65+j)) + str(i+1)
	return tuple((gamescore, move, action, my_next_move))

def minimax_max(current_state, n, current_player, op_player, depth):
	if depth==cutoff_depth:
		return tuple((calc_gamescore(current_state), None, None, None))

	gamescore = -float('infinity')
	my_next_move = None
	temp_next_state = None
	free_spots_present = 0

	for i in range(n):
		for j in range(n):
			if current_state[i][j]=='.':
				if free_spots_present==0:
					free_spots_present = 1
				temp_next_state = resulting_state(current_state, n, i, j, current_player, op_player, 'Stake')
				temp = max(gamescore, minimax_min(temp_next_state[0], n, op_player, current_player, depth+1)[0])
				if temp!=gamescore:
					gamescore = temp
					my_next_move = temp_next_state[0]
					action = 'Stake'
					move = str(chr(65+j)) + str(i+1)

	if free_spots_present==0:
		return tuple((calc_gamescore(current_state), None, None, None))

	for i in range(n):
		for j in range(n):
			flag = 0
			if current_state[i][j]=='.':
				
				if (i+1)<n:
					if current_state[i+1][j]==current_player:
						flag = 1
				if (i-1)>=0:
					if current_state[i-1][j]==current_player:
						flag =  1
				if (j+1)<n:
					if current_state[i][j+1]==current_player:
						flag = 1
				if (j-1)<n:
					if current_state[i][j-1]==current_player:
						flag = 1

				if flag==1:
					temp_next_state = resulting_state(current_state, n, i, j, current_player, op_player, 'Raid')
					temp = max(gamescore, minimax_min(temp_next_state[0], n, op_player, current_player, depth+1)[0])
					if temp!=gamescore:
						gamescore = temp
						my_next_move = temp_next_state[0]
						if temp_next_state[1]==1:
							action = 'Raid'
						else:
							action = 'Stake'
						move = str(chr(65+j)) + str(i+1)
	return tuple((gamescore, move, action, my_next_move))

def alphabeta_min(current_state, alpha, beta, n, current_player, op_player, depth):
	if depth==cutoff_depth:
		return tuple((calc_gamescore(current_state), None, None, None))

	gamescore = float('infinity')
	my_next_move = None
	temp_next_state = None
	free_spots_present = 0

	for i in range(n):
		for j in range(n):
			if current_state[i][j]=='.':
				if free_spots_present==0:
					free_spots_present = 1
				temp_next_state = resulting_state(current_state, n, i, j, current_player, op_player, 'Stake')
				temp = min(gamescore, alphabeta_max(temp_next_state[0], alpha, beta, n, op_player, current_player, depth+1)[0])
				if temp!=gamescore:
					gamescore = temp
					my_next_move = temp_next_state[0]
					action = 'Stake'
					move = str(chr(65+j)) + str(i+1)

					if gamescore<=alpha:
						return tuple((gamescore, move, action, my_next_move))
					beta = min(beta, gamescore)

	if free_spots_present==0:
		return tuple((calc_gamescore(current_state), None, None, None))

	for i in range(n):
		for j in range(n):
			flag = 0
			if current_state[i][j]=='.':
				
				if (i+1)<n:
					if current_state[i+1][j]==current_player:
						flag = 1
				if (i-1)>=0:
					if current_state[i-1][j]==current_player:
						flag =  1
				if (j+1)<n:
					if current_state[i][j+1]==current_player:
						flag = 1
				if (j-1)<n:
					if current_state[i][j-1]==current_player:
						flag = 1

				if flag==1:
					temp_next_state = resulting_state(current_state, n, i, j, current_player, op_player, 'Raid')
					temp = min(gamescore, alphabeta_max(temp_next_state[0], alpha, beta, n, op_player, current_player, depth+1)[0])
					if temp!=gamescore:
						gamescore = temp
						my_next_move = temp_next_state[0]
						if temp_next_state[1]==1:
							action = 'Raid'
						else:
							action = 'Stake'
						move = str(chr(65+j)) + str(i+1)

						if gamescore<=alpha:
							return tuple((gamescore, move, action, my_next_move))
						beta = min(beta, gamescore)
	return tuple((gamescore, move, action, my_next_move))

def alphabeta_max(current_state, alpha, beta, n, current_player, op_player, depth):
	if depth==cutoff_depth:
		return tuple((calc_gamescore(current_state), None, None, None))

	gamescore = -float('infinity')
	my_next_move = None
	temp_next_state = None
	free_spots_present = 0

	for i in range(n):
		for j in range(n):
			if current_state[i][j]=='.':
				if free_spots_present==0:
					free_spots_present = 1
				temp_next_state = resulting_state(current_state, n, i, j, current_player, op_player, 'Stake')
				temp = max(gamescore, alphabeta_min(temp_next_state[0], alpha, beta, n, op_player, current_player, depth+1)[0])
				if temp!=gamescore:
					gamescore = temp
					my_next_move = temp_next_state[0]
					action = 'Stake'
					move = str(chr(65+j)) + str(i+1)

					if gamescore>=beta:
						return tuple((gamescore, move, action, my_next_move))
					alpha = max(alpha, gamescore)

	if free_spots_present==0:
		return tuple((calc_gamescore(current_state), None, None, None))

	for i in range(n):
		for j in range(n):
			flag = 0
			if current_state[i][j]=='.':
				
				if (i+1)<n:
					if current_state[i+1][j]==current_player:
						flag = 1
				if (i-1)>=0:
					if current_state[i-1][j]==current_player:
						flag =  1
				if (j+1)<n:
					if current_state[i][j+1]==current_player:
						flag = 1
				if (j-1)<n:
					if current_state[i][j-1]==current_player:
						flag = 1

				if flag==1:
					temp_next_state = resulting_state(current_state, n, i, j, current_player, op_player, 'Raid')
					temp = max(gamescore, alphabeta_min(temp_next_state[0], alpha, beta, n, op_player, current_player, depth+1)[0])
					if temp!=gamescore:
						gamescore = temp
						my_next_move = temp_next_state[0]
						if temp_next_state[1]==1:
							action = 'Raid'
						else:
							action = 'Stake'
						move = str(chr(65+j)) + str(i+1)

						if gamescore>=beta:
							return tuple((gamescore, move, action, my_next_move))
						alpha = max(alpha, gamescore)
	return tuple((gamescore, move, action, my_next_move))

inputFile = 'input.txt'
outputFile = 'output.txt'
file = open(outputFile, 'w')

info = list()

with open(inputFile) as f:
	for line in f.readlines():
		info.append(line.strip())

n = int(info[0])
mode = info[1]
you_play = info[2]

if you_play=='X':
	op_play = 'O'
else:
	op_play = 'X'

cutoff_depth = int(info[3])

board_positions = list()

for i in range(4,4+n):
	board_values.append(list(map(int, info[i].split())))

for i in range(4+n,4+n+n):
	board_positions.append(list(map(str, info[i])))


if mode=="MINIMAX":
	answer_tup = minimax_max(board_positions, n, you_play, op_play, 0)
elif mode=="ALPHABETA":
	answer_tup = alphabeta_max(board_positions, -float('infinity'), float('infinity'), n, you_play, op_play, 0)


file.write(answer_tup[1] + " " + answer_tup[2])
for i in range(n):
	file.write("\n" + ''.join(answer_tup[3][i]))