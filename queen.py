# grid =          [[0,0,0,0],
#                 [0,0,0,0],
#                 [0,0,0,0],
#                 [0,0,0,0]]
import numpy as np

num = int(input("Enter the number of queens: "))

def main():
    grid = np.zeros((num,num),dtype= "int")
    print("The initial result: ")
    print_values(grid)
    solve(grid,0)
    print("The final result:")
    print_values(grid)

def check_valid(grid):
    number = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i][j] == 1):
                number = number + 1
    if (num == number ):
        return True
    return False

def print_values(grid):
    for i in range(len(grid)):
        for j in range (len(grid)):
            print(grid[i][j],end =" | ")
        print("\n")

def find_valid_points(grid,row,col):

    for i in range(len(grid)):
        if(grid[row][i] == 1 ):
            return False
    for i in range(len(grid)):
        if (grid[i][col] == 1):
            return False

    #check the upper diagonal on right side
    for i, j in zip(range(row, -1, -1),  range(col, -1, -1)):
        if grid[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, num, 1),  range(col, -1, -1)):
        if grid[i][j] == 1:
            return False
    return True


def solve(grid,col):

    if (check_valid(grid)):
        return True

    for i in range(len(grid)):
        if (find_valid_points(grid,i,col)):
            grid[i][col] = 1

            if (solve(grid,col+1)):
                return True

            grid[i][col] = 0
    return False


main()
