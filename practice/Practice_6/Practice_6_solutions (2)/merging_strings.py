# COMP9021 Practice 6 - Solutions


'''
Say that two strings s_1 and s_2 can be merged into a third string s_3
if s_3 is obtained from s_1 by inserting arbitrarily in s_1 the characters in s_2,
respecting their order. For instance, the two strings ab and cd can be merged
into abcd, or cabd, or cdab, or acbd, or acdb..., but not into adbc nor into cbda.

Prompts the user for 3 strings and displays the output as follows:
- If no string can be obtained from the other two by merging, then the program
  outputs that there is no solution.
- Otherwise, the program outputs which of the strings can be obtained
  from the other two by merging.
'''
#整体思路
#可以通过两个条件判断
#1.三个string中，如果短的两个长度合计数！=最长的长度，肯定无法merge
#2.

def can_merge(string_1, string_2, string_3):
    
    if not string_1 and string_2 == string_3:
        return True
    if not string_2 and string_1 == string_3:
        return True
    if not string_1 or not string_2:
        return False
    #如果第一个string的第一个字母=第三个string的第一个字母
    #再对比除这两个字母其他的字母
    if string_1[0] == string_3[0] and can_merge(string_1[1: ], string_2, string_3[1: ]):
        return True
    if string_2[0] == string_3[0] and can_merge(string_1, string_2[1: ], string_3[1: ]):
        return True
    return False
#将输入的三个string 放入一个list中
ranks = 'first', 'second', 'third'
strings = [input(f'Please input the {rank} string: ') for rank in ranks]
#先判断哪个string是最长的
longest_string_index = 0
#如果第二个string最长，记录下来这个string的index
if len(strings[1]) > len(strings[0]):
    longest_string_index = 1
#再接着对比第三个string和第一第二中较长的
if len(strings[2]) > len(strings[longest_string_index]):
    longest_string_index = 2
#如果第一个sting长度是最
if longest_string_index == 0:
    lats_string1_index, lats_string2_index = 1, 2
#如果第二个sting长度是最
elif longest_string_index == 1:
    lats_string1_index, lats_string2_index = 0, 2
#如果第三个sting长度是最
else:
    lats_string1_index, lats_string2_index = 0, 1
#如果最长的那个string 不等于 另外两个字符串相加，肯定无法merge。或者也不存在can_merge的那些情况，则无解
if len(strings[longest_string_index]) != len(strings[lats_string1_index]) + len(strings[lats_string2_index]) or\
                                      not can_merge(strings[lats_string1_index], strings[lats_string2_index], strings[longest_string_index]):
    print('No solution')
else:
    print(f'The {ranks[longest_string_index]} string can be obtained by merging the other two.')


    
