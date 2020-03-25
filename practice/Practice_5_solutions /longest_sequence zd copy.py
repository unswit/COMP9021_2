# COMP9021 Practice 5 - Solutions


'''
Prompts the user for a string w of lowercase letters and outputs the longest
sequence of consecutive letters that occur in w, but with possibly other letters
in between, starting as close as possible to the beginning of w.
'''


import sys


word = input('Please input a string of lowercase letters: ')
list_len=[]
first=word[0]

list_len.append([word[0]])
for second in word[1:]:
    if ord(second)==ord(first)+1:
        list_len[-1].append(second)
    else:
        list_len.append([second])
    first = second
max_len=0
len_word=0
max_word = []
for l in list_len:
    len_word = len(l)
    if len_word > max_len:
        max_len = len_word
        max_word.append(''.join(l))
print(max_len)
print(max_word[-1])
    
        
