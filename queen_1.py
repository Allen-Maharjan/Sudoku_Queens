import numpy as np
grid = [[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0]]
num = 4

def main ():
    point = []
    for i in range (0,4):
        point.append([0,i])
        point.append([i,0])
        m = grid.diagonal()
        print (m)

main()