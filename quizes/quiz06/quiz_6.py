# COMP9021 19T3 - Rachid Hamadi
# Quiz 6 *** Due Thursday Week 8
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


def get_all_grid_one(current_row_index,
                     current_column_index, row_height, column_width):
    if grid:
        row_length = len(grid)
        column_length = len(grid[0])

        # for row in grid:
        # for item in row:
        #    if item == 0:
        #        return False
        if current_row_index == 8 and current_column_index == 5 and \
                row_height == 2 and column_width == 2:
            print("test")

        for row_index in range(row_length):
            if current_row_index <= row_index < current_row_index + row_height:
                for column_index in range(column_length):
                    if current_column_index <= column_index < current_column_index + column_width and \
                            grid[row_index][column_index] == 0:
                        return 0

        # for row in grid:
        #    if not all(row):
        #        return False

        # return all([all(row) for row in grid])

        # any([1,0,0,0])

        return row_height * column_width

    return 0

def get_all_grid_right_one(current_row_index,
                     current_column_index, row_height, column_width):
    if grid:
        row_length = len(grid)
        column_length = len(grid[0])

        # for row in grid:
        # for item in row:
        #    if item == 0:
        #        return False
        # get right parallelogram

        result = []
        for row_index in range(current_row_index, current_row_index + row_height):
            for column_index in range(current_column_index + row_index - current_row_index,current_column_index + column_width):
                if grid[row_index][column_index] == 0:

                    return 0

        # for row in grid:
        #    if not all(row):
        #        return False

        # return all([all(row) for row in grid])

        # any([1,0,0,0])

        return result

    return [0]

def get_current_point_parallelogram(row_index,column_index):
    left_row_length = len(grid) - row_index
    left_column_length = len(grid[0]) - column_index
    result = []

    for row_height in range(2,left_row_length + 1):
        for column_width in range(2,left_column_length + 1):
            number = get_all_grid_one(row_index,column_index,row_height,column_width)
            result.append(number)
    return result

def size_of_largest_parallelogram():

    # REPLACE PASS ABOVE WITH YOUR CODE
    result = []
    if grid:
        for row_index in range(len(grid)):
            for column_index in range(len(grid[0])):
                if grid[row_index][column_index] == 1:
                    result_list = get_current_point_parallelogram(row_index,column_index)
                    result.extend(result_list)
    if result:
        return max(result)
    else:
        return 0


# POSSIBLY DEFINE OTHER FUNCTIONS


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
