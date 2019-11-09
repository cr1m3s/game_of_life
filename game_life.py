import numpy
import matplotlib.pyplot as plt

universe = numpy.zeros((6, 6))
beacon = [[1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, 1]]
universe[1:5, 1:5] = beacon

rows = universe.shape[0]
cols = universe.shape[1]


while True:
    new_universe = numpy.zeros((6, 6))
    for x in range(0, rows):
        for y in range(0, cols):
            num_neighbours = 0
            if x + 1 < rows:
                if universe[x + 1, y] == 1:
                    num_neighbours += 1
            if y + 1 < cols:
                if universe[x, y + 1] == 1:
                    num_neighbours += 1
            if x + 1 < rows and y + 1 < cols:
                if universe[x + 1, y + 1] == 1:
                    num_neighbours += 1
            if x - 1 < rows:
                if universe[x - 1, y] == 1:
                    num_neighbours += 1
            if y - 1 < cols:
                if universe[x, y - 1] == 1:
                    num_neighbours += 1
            if x - 1 < rows and y + 1 < cols:
                if universe[x - 1, y + 1] == 1:
                    num_neighbours += 1
            if x + 1 < rows and y - 1 < cols:
                if universe[x + 1, y - 1] == 1:
                    num_neighbours += 1
            if universe[x, y] and not 2 <= num_neighbours <= 3:
                new_universe[x, y] = 0
            elif num_neighbours == 3:
                new_universe[x, y] = 1

    plt.imshow(new_universe, cmap='binary')
    plt.show()
