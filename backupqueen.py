initial_grid = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]


counter = 0

def main():
    #let us consider four queens which should not attack each other
    counter1 = 0
    q = [1,1,1,1]
    print(initial_grid)
    #putting the queen in the initial grid
    for i in range (0,len(q)):
        initial_grid[i][0]= q[i]
    print(initial_grid)
    for i in range (0,len(q)):
        if(calculation(initial_grid,len(q),i)==1):
            if (i>0):
                i = i - 1
            if (counter1 == -3):
                counter1 = 0
            counter1 = counter1 + 1
        if (counter == 0):
            if (i == 3):
                counter1 = -3
                print('maharjan')
            initial_grid[i][0] = 0
            initial_grid[i][counter1+i] = 1
                
    print(initial_grid)
    
    
def calculation(initial_grid,num,i):        
        for j in range (0,num):
            if (initial_grid[i][j] == 0 or initial_grid[j][i] == 0 ):
                counter = 0
                print('name')
            #if((i+j)<4 or (j+1)<4):
                #if (initial_grid[i+j][j+1] == 0):
                 #   counter = 0
            else:
                print('allen is my name')
                counter = 1
                break
        return counter
        
main()
