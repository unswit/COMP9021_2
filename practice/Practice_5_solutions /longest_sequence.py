# COMP9021 Practice 5 - Solutions


'''
Prompts the user for a string w of lowercase letters and outputs the longest
sequence of consecutive letters that occur in w, but with possibly other letters
in between, starting as close as possible to the beginning of w.
'''


import sys


word = input('Please input a string of lowercase letters: ')
if not all(c.islower() for c in word):
    print('Incorrect input.')
    sys.exit()

longest_length=：
#最终取值起点：
start =None
#遍历过程中取值起点：
current_start = 0
#总体思路，将word的第一位字母设为起点，逐个遍历word中的字母，每次都用遍历的字母对比上一个字母，如果是连续的length就+1，如果不是也继续遍历
#只不过length不增加，再将word中的第二个字母设为起点，逐个往后遍历，道理同上。

#如果现在遍历的起点位置到word中最后一个单词的位置已经不能超过取出的现有单词组长度时候，就不用遍历啦，因为也不会长过longest_length了
#当遍历的起点位置大于(总长度-现在取出的最长单词长度)之前，这个循环就可以停止了，如果没停止，那curretn_start就得一直往上+1
while current_start < len(word)-longest_length:
    #刚开始会有至少一个作为start的字母，所以长度为1，每次遍历current_start+1(可以看到最后有一个current_start += 1不能忘
    current_length = 1
    #因为需要两两字母对比是否连续，所有标记一下每次遍历的单词，last_in_sequence
    last_in_sequence = ord(word[current_start])
    #挨个对word里的字母用index遍历，index的起点就是current_start点的后一个字母对应的index，终点就是word中的最后一个字母的index
    for i in range(current_start+1,len(word)):
        #如果先在的字母ord比上一个字母的ord大1，说明他们连续
        if ord(word[i])-last_in_sequence==1:
               # 所以现在得到的长度就要+1，如果不是连续，lenth不加，但是current_start是一直要+1的
               current_length +=1
               #sequence中最后一个字母用于下次对比的，就要变成此时的这个字母
               last_in_sequence = ord(word[i])
    if current_length > longest_length:
        longest_length = current_length
        #start 也要变，变成longest——length拥有的stat
        start = current_start
    #需要讨论遍历到最后两个的时候的特殊情况
    while current_start < len(word) - 1 and\
                                       ord(word[current_start + 1]) - ord(word[current_start]) == 1:
        current_start +=1
    current_start += 1
print('The solution is :',''.join(chr(ord(word[start])+i) for i in range(longest_length)))
               
