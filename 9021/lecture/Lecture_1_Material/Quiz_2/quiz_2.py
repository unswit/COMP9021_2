# COMP9021 19T3 - Rachid Hamadi
# Quiz 2 *** Due Thursday Week 3


import sys
from random import seed, randrange
from pprint import pprint

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
# if key = value print mapping

#方法一
import sys
from random import seed, randrange
from pprint import pprint

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
from collections import defaultdict #cycles_key=defaultdict(list)
cycles_key = keys.copy()#This is a list
print("cycles_key:",cycles_key)
while cycles_key:
      first_number = cycles_key[0]  # first_number= the first key in cycles_key
      #print("first_number1:",first_number)
      check = []
      while first_number in cycles_key:
            cycles_key.remove(first_number)  # remove the first number
            check.append(first_number)  # put in check
            first_number = mapping[first_number] # output first_number's value
            #print("first_number:",first_number)
            #print("check:",check)
            if first_number in check:
               first_number_location = check.index(first_number)#list.index(first_number)：the index of first_number
               check = check[first_number_location:]
               mi = min(check)
               #print("mi:",mi)
               check.insert(0,mi)
               #print("check2:",check)
               new_check = []
               for i in check:
                   if i not in new_check:
                      new_check.append(i)
               #print("new_check:",new_check)
               cycles.append(new_check)

reversed_dict = defaultdict(list)
for key, value in mapping.items():
    reversed_dict[value].append(key)

reversed_dict2 = defaultdict(dict)

for key, value in reversed_dict.items():
     reversed_dict2[len(value)].update({key:value})

reversed_dict_per_length = dict(reversed_dict2)


print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)


