# Written by *** and Eric Martin for COMP9021

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
num = '0' * nb_of_leading_zeroes + f'{int(code):o}'


# 分别表示8个方向
directions = [(0, 1), (1, 1), (1, 0), (1, -1),
              (0, -1), (-1, -1), (-1, 0), (-1, 1)]


current_x, current_y = (0, 0)
points = {(current_x, current_y): 1}

for item in reversed(num):
    direction_x, direction_y = directions[int(item)]
    current_x = current_x + direction_x
    current_y = current_y + direction_y
    if (current_x, current_y) not in points:
        points[(current_x, current_y)] = 1
    else:
        del points[(current_x, current_y)]

keys = points.keys()

if keys:
    axis = list(zip(*keys))
    lines = []
    for y in range(min(axis[1]), max(axis[1]) + 1):
        line = ""
        for x in range(min(axis[0]), max(axis[0]) + 1):
            line += on if (x, y) in points else off
        lines.append(line)

    for line in reversed(lines):
        print(line)
