# COMP9021 19T3 - Rachid Hamadi
# Quiz 7 *** Due Thursday Week 9
#
# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).


from random import seed, randrange
import sys

from collections import defaultdict

dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s
# that make it with 2. We "colour" the second shape we find by
# replacing all the 1s that make it with 3.
def colour_shapes():
    colour_index = 3
    # left ,right, down,up
    directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
    for start_column in range(0,10):
        for start_row in range(0,10):
            if grid[start_row][start_column] == 1:#起点为1
                path = [(start_row, start_column)]#路径就是
                while path:
                    # current point
                    (current_row, current_column) = path.pop()#让最后一个点作为起始点
                    for (direction_row, direction_column) in directions:
                        next_row, next_column = direction_row + current_row, direction_column + current_column
                        if next_row in range(0,10) and next_column in range(0,10):
                            if grid[next_row][next_column] != 1:
                                pass
                            else:
                                path.append((next_row, next_column))

                    grid[current_row][current_column] = colour_index#染色

                colour_index += 1
    return colour_index


def max_number_of_spikes(nb_of_shapes):
    result = 0
    directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
    spikes = defaultdict(int)
    for start_column in range(10):
        for start_row in range(10):
            value = grid[start_row][start_column]
            if value == 0:
               pass
            else:
                count = 0
                for (direction_row, direction_column) in directions:
                    next_row, next_column = direction_row + start_row, direction_column + start_column
                    if next_row in range(0,10) and next_column in range(0,10):
                       if grid[next_row][next_column] == value:
                          count += 1
                       else:
                           pass
                if count == 1:
                    spikes[value] += 1

    if nb_of_shapes and spikes.values():
        result = max(spikes.values())

# Possibly define other functions here    


try: 
    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
     )
