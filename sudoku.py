#Sudoku Solver


values = [
    [0,8,0,4,0,0,1,2,0],
    [0,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def printvalues(val,printout): #function for printing the values in sudoku manner
	print(printout)
	for i in range(0,len(val)):
		for j in range(0,len(val)):
			if(j%3 == 0 ):
				print("|",end=' ')
			print(val[i][j],end =" ")
		if(i%3 == 2 and i!=0):
			print("\n------------------------")
		else:
			print("\n")

def find_empty(board): #function for finding the empty place of sudoku in our model its 0
	for i in range(0,len(board)):
		for j in range(0,len(board)):
			if (board[i][j] == 0):
				return (i,j)
	return None

def check(board, number, pos): #to check whether the number about to entered is valid

	#for row
	for i in range (len(board)):
		if (board[pos[0]][i] == number and pos[1]!= i):
			return False

	#for column
	for i in range(len(board)):
		if (board[i][pos[1]] == number and pos[0] != i ):
			return False

	#for checking in the 3X3 box
	box_x = pos[1] // 3 #using floor devision
	box_y = pos[0] // 3
	for i in range(box_y*3, box_y*3 + 3):
		for j in range(box_x*3, box_x*3 + 3 ):
			if (board[i][j] == number and (i,j) != pos):
				return False
	return True

def solve(board): #using recursion and backtracking
	find = find_empty(board)
	if (find == None ):
		return True
	else:
		row , col = find
		for i in range (1,10):
			if check(board,i, (row,col)):
				board[row][col] = i

				if solve(board): #recursively calling function
					return True

			board[row][col] = 0
	return False



printvalues(values,"The Initial Solution: ")
solve(values)
printvalues(values,"The Final Solution: ")
