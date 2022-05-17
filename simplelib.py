from variables import *
import copy

def countChain (board, stone) :
#def countChain( board : list[list[int]], stone : int = BLACK ) -> tuple[ list[list[int]], list[list[int]], list[list[int]], list[list[int]] ] :
	
	isYours = [ [ int(grid == stone) for grid in row ] for row in board ]	
	rowChain = isYours
	colChain = copy.deepcopy(isYours)
	topleftChain = copy.deepcopy(isYours)
	toprightChain = copy.deepcopy(isYours)

	for i in range(BOARDSIZE) :
		for j in range(BOARDSIZE) :
			if (j != 0 and rowChain[i][j]):
				rowChain[i][j] = rowChain[i][j-1] + 1
			if (i != 0 and colChain[i][j]):
				colChain[i][j] = colChain[i-1][j] + 1
			if (i != 0 and j != 0 and topleftChain[i][j]):
				topleftChain[i][j] = topleftChain[i-1][j-1] + 1;
			if (i != 0 and j != BOARDSIZE-1 and toprightChain[i][j]) :
				toprightChain[i][j] = toprightChain[i-1][j+1] + 1
				
	for i in range(BOARDSIZE-1,-1,-1) :
		for j in range(BOARDSIZE-1,-1,-1) :
			if (j != BOARDSIZE-1 and rowChain[i][j] and rowChain[i][j+1]) :
				rowChain[i][j] = rowChain[i][j+1] 
			if (i != BOARDSIZE-1 and rowChain[i][j] and rowChain[i+1][j]) :
				colChain[i][j] = colChain[i+1][j]
			if (i != BOARDSIZE-1 and j != BOARDSIZE-1 and topleftChain[i][j] and topleftChain[i+1][j+1]) :
				topleftChain[i][j] = topleftChain[i+1][j+1];
			if (i != BOARDSIZE-1 and j != 0 and toprightChain[i][j] and toprightChain[i+1][j-1]) :
				toprightChain[i][j] = toprightChain[i+1][j-1]
	return rowChain, colChain, topleftChain, toprightChain