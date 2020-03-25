# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).
#
# Written by *** and Eric Martin for COMP9021


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
    # pass
    # Replace pass above with your code
    colour_index = 2
    # top, right ,bottom, left
    directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
    for y in range(dim):
        for x in range(dim):
            if grid[y][x] == 1:
                path = [(x, y)]
                while path:
                    # current point
                    (current_x, current_y) = path.pop()
                    for (direction_x, direction_y) in directions:
                        next_x, next_y = direction_x + current_x, direction_y + current_y
                        if 0 <= next_x < dim and 0 <= next_y < dim and grid[next_y][next_x] == 1:
                            path.append((next_x, next_y))

                    grid[current_y][current_x] = colour_index

                colour_index += 1

    return colour_index


def max_number_of_spikes(nb_of_shapes):
    # Replace pass above with your code
    result = 0
    directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
    spikes = defaultdict(int)
    for y in range(dim):
        for x in range(dim):
            value = grid[y][x]
            if value > 0:
                count = 0
                # current point
                for (direction_x, direction_y) in directions:
                    next_x, next_y = direction_x + x, direction_y + y
                    if 0 <= next_x < dim and 0 <= next_y < dim and grid[next_y][next_x] == value:
                        count += 1
                if count == 1:
                    spikes[value] += 1

    if nb_of_shapes and spikes.values():
        result = max(spikes.values())

    return result


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
