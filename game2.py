import os
import time

FIELD = 38
universe = [[0]*FIELD for i in range(FIELD)]
'''
#block
universe[1][1] = 1
universe[2][2] = 1
universe[1][2] = 1
universe[2][1] = 1

#line
universe[20][0] = 1
universe[20][1] = 1
universe[20][2] = 1

#tub
universe[10][5] = 1
universe[11][4] = 1
universe[11][6] = 1
universe[12][5] = 1
#boat
universe[15][4] = 1
universe[15][5] = 1
universe[16][4] = 1
universe[16][6] = 1
universe[17][5] = 1


#oscil
universe[4][3] = 1
universe[5][3] = 1
universe[6][3] = 1
universe[7][3] = 1
universe[8][3] = 1
universe[4][4] = 1

#beacon
universe[5][5] = 1
universe[5][6] = 1
universe[6][5] = 1
universe[8][7] = 1
universe[8][8] = 1
universe[7][8] = 1

#horizontal
universe[1][1] = 1
universe[1][2] = 1
universe[1][3] = 1
'''

#glinder gun
universe[5][1] = 1
universe[6][1] = 1
universe[5][2] = 1
universe[6][2] = 1

universe[5][11] = 1
universe[6][11] = 1
universe[7][11] = 1
universe[4][12] = 1
universe[8][12] = 1
universe[3][13] = 1
universe[9][13] = 1
universe[3][14] = 1
universe[9][14] = 1
universe[6][15] = 1
universe[4][16] = 1
universe[8][16] = 1
universe[5][17] = 1
universe[6][17] = 1
universe[7][17] = 1
universe[6][18] = 1

universe[5][21] = 1
universe[4][21] = 1
universe[6][21] = 1
universe[5][22] = 1
universe[4][22] = 1
universe[6][22] = 1

universe[3][23] = 1
universe[7][23] = 1

universe[3][25] = 1
universe[7][25] = 1

universe[2][25] = 1
universe[8][25] = 1

universe[3][35] = 1
universe[4][35] = 1
universe[3][36] = 1
universe[4][36] = 1




rows = len(universe)
cols = len(universe[0])

def print_list(arr):
    for i in range(len(arr)):
        for j in  range(len(arr[i])):
            if arr[i][j] == 1:
                print('\033[92m' + ' #' + '\033[0m', end = '')
            else:
                print('\033[91m' + ' *' + '\033[0m', end='')
        print()
print_list(universe)


for a in range(1000):
    time.sleep(0.1)
    os.system('clear')
    print(f"{a} iteration:")
    new_universe = [[0]*FIELD for i in range(FIELD)]
    
    for x in range(len(universe)):
        for y in range(len(universe[x])):
           
            num_neighbours = 0 
            if x + 1 < rows: 
                if universe[x + 1][y] == 1: 
                    num_neighbours += 1 
            if y + 1 < cols: 
                if universe[x][y + 1] == 1: 
                    num_neighbours += 1 
            if x + 1 < rows and y + 1 < cols: 
                if universe[x + 1][y + 1] == 1: 
                    num_neighbours += 1 
            if x - 1 >= 0: 
                if universe[x - 1][y] == 1: 
                    num_neighbours += 1 
            if y - 1 >= 0: 
                if universe[x][y - 1] == 1: 
                    num_neighbours += 1 
            if x - 1 >= 0 and y + 1 < cols: 
                if universe[x - 1][y + 1] == 1: 
                    num_neighbours += 1 
            if x + 1 < rows and y - 1 >= 0: 
                if universe[x + 1][y - 1] == 1: 
                    num_neighbours += 1
            if x - 1 >= 0 and y - 1 >= 0:
                if universe[x - 1][y - 1] == 1:
                    num_neighbours += 1
            if universe[x][y] and not 2 <= num_neighbours <= 3: 
                new_universe[x][y] = 0 
            elif num_neighbours == 3: 
                new_universe[x][y] = 1
            elif universe[x][y]  and  num_neighbours == 2:
                new_universe[x][y] = 1
    
    universe = list(new_universe)
    print_list(new_universe)
