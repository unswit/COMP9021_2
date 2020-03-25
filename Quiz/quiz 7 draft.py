# How many integers are there between 1 and 1000 which are divisible by 6 or 15 but not both?
from random import seed, randrange
import sys

def display_grid():
    for row in grid:
        print('   ', *row)

def find_left(current_row,current_column):#向左找到不能找为止
    number = 0
    if 0 < current_column:
        if grid[current_row][current_column-1]==1:
            number += 1
            return number
        else:
            return 0
    else:
        return 0

def find_right(current_row,current_column):
    number = 0
    if current_column < 10:
        if grid[current_row][current_column+1]==1:
            number += 1
            return number
        else:
            return 0
    else:
        return 0

def find_down(current_row,current_column):
    number = 0
    if current_row < 10:
        if grid[current_row+1][current_column]==1:
            number += 1
            return number
        else:
            return 0
    else:
        return 0

def find_up(current_row,current_column):
    number = 0
    if 0 < current_row:
        if grid[current_row-1][current_column]==1:
            number += 1
            return number
        else:
            return 0
    else:
        return 0

def colour_shapes(current_row,current_column):
    count_spike = 0
    number = find_left(current_row,current_column) + find_right(current_row,current_column) \
             + find_up(current_row,current_column) + find_down(current_row,current_column)#sum 所有方向有几个1
    if number ==1 or number == 0:
       count_spike +=1
        return 1
    else:
        return 0

def max_number_of_spikes(nb_of_shapes):
    spikes = []
    if grid:
       for current_row in range(10):
           for current_column in range(10):
               if grid[current_row][current_column]==1:#如果现在点=1 ，就去找color是不是 >3
                  spikes = colour_shapes(current_row,current_column)
    if number:
        return number
    else:
        return 0


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
grid = [[int(randrange(density) != 0) for _ in range(10)]
            for _ in range(10)
       ]
print('Here is the grid that has been generated:')

display_grid()
nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
     )

# def colour_shapes(current_row,current_column):
    # number = 0
    # if current_column>0 and grid[current_row][current_column-1]==1:
    #     number += 1
    # else:
    #     continue
    #     if current_row >0 and grid[current_row-1][current_column]==1:
    #         number +=1
    #         if current_row