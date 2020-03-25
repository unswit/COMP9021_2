# COMP9021 19T3 - Rachid Hamadi
# Quiz 3 *** Due Thursday Week 4


# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE
# get the direction number
code_read_as = '0' * nb_of_leading_zeroes + f'{int(code):o}'
direction_num = list(map(str,reversed(code_read_as)))

# set up the direction number 0-7
dic = {"0":(0,1),"1":(1,1),"2":(1,0),"3":(1,-1),"4":(0,-1),"5":(-1,-1),"6":(-1,0),"7":(-1,1)}

#Axis origin
Axis_origin_x = 0
Axis_origin_y = 0

from collections import defaultdict
path = {(0,0):on}

for i in direction_num:
    x,y = dic[i]
    Axis_origin_x += x
    Axis_origin_y += y
    #print(Axis_origin_x, Axis_origin_y)
    if (Axis_origin_x,Axis_origin_y) in path:
        del path[(Axis_origin_x, Axis_origin_y)]
    elif (Axis_origin_x,Axis_origin_y) not in path:
        path[(Axis_origin_x, Axis_origin_y)] = on
    else:
        path[(Axis_origin_x, Axis_origin_y)] = "\n"

#print("path:",path)

west = south= 0
north = east = -1
path_list = list(path.keys())
for i in path_list:
    x,y = i
    west = min(x,west)
    north = max(y,north)
    east = max(x,east)
    south = min(y,south)


for y in range(north,south -1,-1):
    for x in range(west,east + 1,1):
        if (x,y) in path_list:
            print(path[(x,y)],end="")
        else:
            print(off,end="")
    if south < y:
        print()
