# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange
from pprint import pprint
from collections import defaultdict

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}
# INSERT YOUR CODE HERE
if keys:
    visited = []
    for key in keys:
        if key in visited:
            continue
        value = mapping.get(key)
        # {1:1}
        # {10:10}
        if key == value:
            cycles.append([key])
            visited.append(key)
        else:
            # {2:3,3:4, 4,2}
            # [2,3]
            # key = 2,value = 3
            new_items = [key, value]
            # {1:4,2:3,3:5,4:6,5:3}
            while value in mapping:
                new_key = value
                # new_key = 3
                value = mapping.get(new_key)
                # value = 4
                # new_items = [2,3]
                if new_items[0] == value:
                    cycles.append(new_items)
                    visited.extend(new_items)
                    break

                if value in new_items:
                    break
                # new_items = [2,3,]
                new_items.append(value)

reversed_dict = defaultdict(list)

reversed_dict['a'].append("1","2")

reversed_dict = {}
if "a" in reversed_dict:
    reversed_dict['a'].append("1","2")
else:
    reversed_dict['a'] = []



# {1:2,3:2}
# {2:[1,3],}
for key, value in mapping.items():
    reversed_dict[value].append(key)


# {2:[3]}
for key, value in reversed_dict.items():
    length = len(value)
    # reversed_dict_per_length = {}
    if length in reversed_dict_per_length:
        reversed_dict_per_length[length][key] = value
    else:
        # {1:{2:[3]}}
        reversed_dict_per_length[length] = {key: value}

print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)
