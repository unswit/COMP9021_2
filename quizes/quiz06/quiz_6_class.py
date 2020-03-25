# Written by *** and Eric Martin for COMP9021
#
# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111


from random import seed, randrange
import sys

dim = 10


def display_grid():
    for row in grid:
        print('   ', *row)


def size_of_largest_parallelogram_third(point, size):
    #      111
    #     111
    #    111
    #   111
    # get the current point
    (x, y) = point
    # check current row and next row
    for height in range(0, 2):
        for width in range(0, size):

            current_x = x + height + width
            current_y = y + height

            if 0 <= current_x < dim and 0 <= current_y < dim and grid[current_y][current_x] == 1:
                continue
            else:
                return 0

    # if current row and next row are all 1
    for height in range(2, len(grid) - y):
        for width in range(0, size):
            current_x = x + height + width
            current_y = y + height
            if 0 <= current_x < dim and 0 <= current_y < dim and grid[current_y][current_x] == 1:
                continue
            else:
                return height * size

    # last line
    return (dim - y) * size


def size_of_largest_parallelogram_two(point, size):
    #      111
    #     111
    #    111
    #   111
    # get the current point
    (x, y) = point
    # check current row and next row
    for height in range(0, 2):
        for width in range(0, size):

            current_x = x - height + width
            current_y = y + height

            if 0 <= current_x < dim and 0 <= current_y < dim and grid[current_y][current_x] == 1:
                continue
            else:
                return 0
    # if current row and next row are all 1
    for height in range(2, len(grid) - y):
        for width in range(0, size):
            current_x = x - height + width
            current_y = y + height
            if 0 <= current_x < dim and 0 <= current_y < dim and grid[current_y][current_x] == 1:
                continue
            else:
                return height * size

    # last line
    return (dim - y) * size


def size_of_largest_parallelogram_one(point, size):
    #      111
    #      111
    #      111
    #      111
    # get the current point
    (x, y) = point
    # check current row and next row
    for height in range(0, 2):
        for width in range(0, size):

            current_x = x + width
            current_y = y + height

            if 0 <= current_x < dim and 0 <= current_y < dim and grid[current_y][current_x] == 1:
                continue
            else:
                return 0
    # if current row and next row are all 1
    for height in range(2, dim - y):
        for width in range(0, size):
            current_x = x + width
            current_y = y + height
            if 0 <= current_x < dim and 0 <= current_y < dim and grid[current_y][current_x] == 1:
                continue
            else:
                return height * size

    # if last line
    return (dim - y) * size


def size_of_largest_parallelogram():
    # REPLACE PASS ABOVE WITH YOUR CODE
    # check current position is 1
    max_size = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                # 1 1 0 0000 1 11
                for size in range(2, dim - x + 1):
                    # check the star length 2
                    first = size_of_largest_parallelogram_one((x, y), size)
                    second = size_of_largest_parallelogram_two((x, y), size)
                    third = size_of_largest_parallelogram_third((x, y), size)
                    max_size = max((max_size, first, second, third))

    return max_size


# POSSIBLY DEFINE OTHER FUNCTIONS

def get_max(line, index, type=1):

    y, x = divmod(index, dim)
    result = 0
    for step in range(2, dim - x + 1):
        height = 0
        temp = index
        y, x = divmod(index, dim)
        while temp < len(line) and line[temp: temp + step] == "1" * step:
            height += 1
            if type == 1:
                temp = (y + 1) * dim + x
            elif type == 2:
                if x == 0:
                    break
                temp = (y + 1) * dim + x - 1
            else:
                if x + 1 == dim:
                    break
                temp = (y + 1) * dim + x + 1

            if temp / dim == y:
                break
            # the same
            y, x = divmod(temp, dim)


        if height > 1:
            result = max(result,height * step)
        else:
            break
    return  result


def size_of_largest_parallelogram_ext():
    line = "".join([str(x) for row in grid for x in row])

    max_size = 0
    for index in range(len(line)):
        if line[index] == "1":
            max_size = max(max_size,get_max(line,index,1))
            max_size = max(max_size,get_max(line, index, 2))
            max_size = max(max_size,get_max(line, index, 3))
    return max_size


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
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
          )
else:
    print('There is no parallelogram with horizontal sides.')
