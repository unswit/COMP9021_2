# COMP9021 19T3 - Rachid Hamadi
# Quiz 1 *** Due Thursday Week 2


import sys
from random import seed, randrange

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}

# {1:2,2:3}


for i in range(1, upper_bound):
    r = randrange(-upper_bound // 2, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)

mapping_as_a_list = []
one_to_one_part_of_mapping = {}
nonkeys = []

# INSERT YOUR CODE HERE
# 知识点总结
# 1.range的用法
# 2。列表的生成
# 3.list的内置函数
# 4。dict的遍历

mapping[1] = 2
for key, value in mapping.items():
    print(key, value)

keys = mapping.keys()
values = mapping.values()

# mapping = {3:1}
inputs = []
for item in range(1, upper_bound):
    if item in mapping:
        continue
    else:
        inputs.append(item)
    # if item not in mapping:
    #    inputs.append(item)
# 1,2,3,4

inputs = [item for item in range(1, upper_bound)]
# 1,2,3,4


# first
nonkeys = [item for item in range(1, upper_bound) if item not in mapping]
# second
# mapping_as_a_list = [None] * upper_bound
# for key, value in mapping.items():
#    mapping_as_a_list[key] = value

# 第二种方法
for item in range(upper_bound):
    if item in mapping:
        mapping_as_a_list.append(mapping[item])
    else:
        mapping_as_a_list.append(None)
# 第三种方法
for item in range(upper_bound):
    mapping_as_a_list.append(None)
# current status
# mapping_as_a_list:[None,None,None,None,None]
for key, value in mapping.items():
    mapping_as_a_list[key] = value
# mapping_as_a_list:[None,None,None,1,None]

# third
# one_to_one_part_of_mapping = {key: value for key, value in mapping.items() if list(mapping.values()).count(value) == 1}
# 最笨的办法
one_to_one_part_of_mapping = {}
for key, value in mapping.items():
    count = 0
    for key1, value1 in mapping.items():
        if value == value1:
            count = count + 1
    if count == 1:
        one_to_one_part_of_mapping[key] = value

# 第三种
keys = mapping.keys()
values = mapping.values()
for key in keys:
    count = 0
    for value in values:
        if mapping[key] == value:
            count += 1
    if count == 1:
        one_to_one_part_of_mapping[key] = mapping[key]

print()
print('EDIT THIS PRINT STATEMENT')
print('\nThe list of integers between 1 and', upper_bound - 1, 'that are not keys of the mapping is:')
print('  ', nonkeys)
print('\nRepresented as a list, the mapping is:')
print('  ', mapping_as_a_list)
# Recreating the dictionary, inserting keys from smallest to largest,
# to make sure the dictionary is printed out with keys from smallest to largest.
one_to_one_part_of_mapping = {key: one_to_one_part_of_mapping[key]
                              for key in sorted(one_to_one_part_of_mapping)
                              }
print('\nThe one-to-one part of the mapping is:')
print('  ', one_to_one_part_of_mapping)
