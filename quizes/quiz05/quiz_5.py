# Written by *** and Eric Martin for COMP9021
#
# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2,
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.


import sys
from collections import deque


def encode(list_of_integers):
    # [10,20,30]

    numbers = []
    for e in list_of_integers:
        # e = 10
        # 1010
        # [11,00,11,00]
        # 11000011000
        # [1100110001000000001101010101]
        numbers.append("".join([item * 2 for item in bin(e)[2:]]))
    result = "0".join(numbers)
    return int(result, 2)


def decode(integer):
    # 给定一个数字，转换成2进制
    # list append(1),pop 1 尾端进行操作，2，3,1， 2，3，1 pop() 1
    # deque 双向链表 append,append left
    # 857310204
    # 11001100   0      11  00  11  00  00  0  11   11  11  11  00
    # 1010              10100                   11110

    # 11110110001100001111110100110011110000
    # 1111 0  11  0001100001111110100110011110000
    number = bin(integer)[2:]

    # check odd number of '1'
    if number.count("1") % 2 == 1:
        return None

    base_deque = deque(bin(integer)[2:])

    line = ''
    while len(base_deque) >= 2:
        first = base_deque.popleft()
        second = base_deque.popleft()
        if first == second:
            line += first
        else:
            line += ' '
            base_deque.appendleft(second)

    result = [int(n, 2) for n in line.split()]
    # 返回结果
    if len(base_deque) == 0 and result:
        return result
    else:
        return None


# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2:])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2:] for e in the_input)}]'
          )
    print('  It is encoded by', encode(the_input))
