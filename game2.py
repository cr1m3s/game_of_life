import os
import time


#block
def block(universe):
    universe[1][1] = 1
    universe[2][2] = 1
    universe[1][2] = 1
    universe[2][1] = 1

    return universe

#line
def line(universe):
    universe[20][0] = 1
    universe[20][1] = 1
    universe[20][2] = 1

    return universe

#tub
def tube(universe):
    universe[10][5] = 1
    universe[11][4] = 1
    universe[11][6] = 1
    universe[12][5] = 1

    return universe


#boat
def boat(universe):
    universe[15][4] = 1
    universe[15][5] = 1
    universe[16][4] = 1
    universe[16][6] = 1
    universe[17][5] = 1
    return universe


#oscil
def oscil(universe):
    universe[4][3] = 1
    universe[5][3] = 1
    universe[6][3] = 1
    universe[7][3] = 1
    universe[8][3] = 1
    universe[4][4] = 1
    return universe


#beacon
def beacon(universe):
    universe[5][5] = 1
    universe[5][6] = 1
    universe[6][5] = 1
    universe[8][7] = 1
    universe[8][8] = 1
    universe[7][8] = 1
    return universe


#horizontal
def horizontal(universe):
    universe[1][1] = 1
    universe[1][2] = 1
    universe[1][3] = 1

    return universe


#glinder gun
def gun(universe):
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
    return universe


def print_list(arr):
    g_start = '\033[92m'
    g_end = '\033[0m'
    print(g_start + '┌' + '──' * len(arr[0]) + '┐' + '\033[0m' + g_end)
    for i in range(len(arr)):
        print(g_start + "│" + '\033[0m' + g_end, end = '')
        for j in  range(len(arr[i])):
            if arr[i][j] == 1:
                print(g_start + '⬛' + '\033[0m' + g_end, end = '')
            else:
                print(g_start + '⬜' + g_end, end='')
        print(g_start + "│" + g_end)
    print(g_start + '└' + '──' * len(arr) + '┘' + g_end)


def game(field, iterations):
    
    universe = [[0]*field for i in range(field)]
    rows = len(universe)
    cols = len(universe[0])
    
    fun = input("Chose figure: gun/horizontal/beacon/block/line/boat/tube/oscil:")
    functions = ["gun", "horizontal", "beacon", "block", "line", "tube", "oscil"]
    
    if fun in functions:
        if fun == "gun":
            universe = gun(universe)
        elif fun == "horizontal":
            universe = horizontal(universe)
        elif fun == "beacon":
            universe = beacon(universe)
        elif fun == "block":
            universe = block(universe)
        elif fun == "line":
            universe = line(universe)
        elif fun == "tube":
            universe = tube(universe)
        else:
            universe = oscil(universe)
    

    for a in range(iterations):
        time.sleep(0.25)
        os.system('clear')
        print(f"{a} iteration:")
        new_universe = [[0]*field for i in range(field)]
        
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


if __name__ == '__main__':
    field = int(input("Enter suze of the field: "))
    iterations = int(input("Enter number of iterations: "))
    game(field, iterations)

    print("THATS ALL FOLKS!")
