import sys
import os
import time
import random
from PIL import Image


# block
def block(universe):
    universe[1][1] = 1
    universe[2][2] = 1
    universe[1][2] = 1
    universe[2][1] = 1

    return universe


# line
def line(universe):
    universe[20][0] = 1
    universe[20][1] = 1
    universe[20][2] = 1

    return universe


# tube
def tube(universe):
    universe[10][5] = 1
    universe[11][4] = 1
    universe[11][6] = 1
    universe[12][5] = 1

    return universe


# boat
def boat(universe):
    universe[15][4] = 1
    universe[15][5] = 1
    universe[16][4] = 1
    universe[16][6] = 1
    universe[17][5] = 1
    return universe


# oscil
def oscil(universe):
    universe[4][3] = 1
    universe[5][3] = 1
    universe[6][3] = 1
    universe[7][3] = 1
    universe[8][3] = 1
    universe[4][4] = 1
    return universe


# beacon
def beacon(universe):
    universe[5][5] = 1
    universe[5][6] = 1
    universe[6][5] = 1
    universe[8][7] = 1
    universe[8][8] = 1
    universe[7][8] = 1
    return universe


# horizontal
def horizontal(universe):
    universe[1][1] = 1
    universe[1][2] = 1
    universe[1][3] = 1

    return universe


# random universe
def ran_gen(universe):
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            universe[i][j] = random.randint(0, 1)

    return universe


# image to universe
def img_to_universe(image):
    width, height = image.size[0], image.size[1]
    aspect_ratio = height / width
    new_height = int(input("Enter new height(10-20 recomended): "))
    new_width = int(new_height / aspect_ratio)

    image = image.resize((new_width, new_height))
    pixels = image.getdata()

    new_pixels = []
    for pixel in pixels:
        if pixel == 0:
            new_pixels.append(1)
        else:
            new_pixels.append(0)
    new_pixels_count = len(new_pixels)

    universe = [new_pixels[index:index + new_width]
                for index in range(0, new_pixels_count, new_width)]
    print_list(universe)
    
    # magic numbers 38 and 35 depends from terminal size
    # my font size in terminal allows smooth work of script only for such
    # numbers 
    new_universe = [[0]*38 for i in range(35)]
    
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            new_universe[i][j] = universe[i][j]

    return new_universe


def print_list(arr):
    g_start = '\033[92m'
    g_end = '\033[0m'
    print(g_start + '┌' + '──' * len(arr[0]) + '┐' + '\033[0m' + g_end)
    for i in range(len(arr)):
        print(g_start + "│" + '\033[0m' + g_end, end='')
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                print(g_start + '⬛' + '\033[0m' + g_end, end='')
            else:
                print(g_start + '⬜' + g_end, end='')
        print(g_start + "│" + g_end)
    print(g_start + '└' + '──' * len(arr[0]) + '┘' + g_end)


def game(iterations, universe=None):
    fun = ''
    if universe:
        fun = "image"
    else:
        field_size = int(input("Enter size of the square universe: "))
        universe = [[0]*field_size for i in range(field_size)]

    rows = len(universe)
    cols = len(universe[0])

    if fun != "image":
        print("Start figures: random/boat/beacon")
        fun = input("Chose figure: ")
        functions = ["random", "horizontal", "beacon",
                     "block", "line", "tube", "oscil"]

        if fun in functions:
            if fun == "horizontal":
                universe = horizontal(universe)
            elif fun == "beacon":
                universe = beacon(universe)
            elif fun == "block":
                universe = block(universe)
            elif fun == "line":
                universe = line(universe)
            elif fun == "tube":
                universe = tube(universe)
            elif fun == "random":
                universe = ran_gen(universe)
            else:
                universe = oscil(universe)

    for a in range(iterations):
        time.sleep(0.1)
        os.system('clear')
        print(f"{a} iteration:")
        new_universe = [[0]*len(universe[0]) for i in range(len(universe))]

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
                elif universe[x][y] and num_neighbours == 2:
                    new_universe[x][y] = 1

        universe = list(new_universe)
        print_list(new_universe)


if __name__ == '__main__':
    image = Image
    universe = None
    if len(sys.argv) > 1:
        image = Image.open(sys.argv[1]).convert('1')
        universe = img_to_universe(image)
    iterations = int(input("Enter number of iterations: "))
    game(iterations, universe)

    print(f"Passed {iterations} iterations of game of life:)")
