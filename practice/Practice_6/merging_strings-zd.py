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
def can_merge(string1,string2,string3):
    if not string1 and string2 == string3:
        return True
    if not string2 and string1==string3:
        return True
    if not string1 or not string2:
        return False
    if string1[0]==string3[0] and can_merge(string1[1:],string2, string3[1:]):
        return True
    if string2[0]==string3[0] and can_merge(string1,string2[1:], string[1:]):
        return True
    return False

ranks = 'first','second','third'
strings = [input(f'Please input the {rank} string: ') for rank in ranks]
longest_string_index = 0
if len(strings[1]) > len(strings[0]):
    longest_string_index = 1
if len(strings[2]) > len(strings[longest_string_index]):
    longest_string_index = 2

if longest_string_index==0:
       last_string1_index, last_string2_index= 1,2
if longest_string_index==1:
       last_string1_index, last_string2_index= 0,2
else:
    last_string1_index, last_string2_index = 0, 1

if len(strings[longest_string_index]) != len(strings[last_string1_index]) + len(strings[last_string2_index]) or\
                                      not can_merge(strings[last_string1_index], strings[last_string2_index], strings[longest_string_index]):
       print('No solution')
else:
    print(f'The {ranks[last_string1_index]} string can be obtained by merging the other two.')
           


