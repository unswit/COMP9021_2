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

def all_point(current_row,
                     current_column, hight, lenth):
    for move_row in range(10):#移动的点move  move_row =0
        if current_row <= move_row < current_row + hight:#如果定点行数<=等于移动点行数<定点行数+高度 （高度范围在2和10-定点行数中间）
            for move_column in range(10):#左右移动范围在1-10
                if current_column <= move_column < current_column + lenth and grid[move_row][move_column] == 0:
                    #定点列数<=移动点的列数<定点列数+长度且 移动点=0
                    return 0
                elif current_column <= move_column < current_column + lenth and grid[move_row][move_column] == 0:
                    return 0
    return hight * lenth

def get_current_point_parallelogram(move_row,move_column):#取所有平行四边形的面积
    result = []
    for hight in range(2,10 - move_row + 1):#high 高度 high 2
        for lenth in range(2,10 - move_column + 1):#宽度 lenth 2
            number = all_point(move_row,move_column,hight,lenth)
            result.append(number)
    return result

def size_of_largest_parallelogram():

    # REPLACE PASS ABOVE WITH YOUR CODE
    result = []
    if grid:
        for move_row in range(10):#row 的范围不能超过grid  move_row = 0
            for move_column in range(10):#column的范围不能超过grid move_colum = 0
                if grid[move_row][move_column] == 1:#如果该点是1
                    result_list = get_current_point_parallelogram(move_row,move_column)#取得该点的平行四边形
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
