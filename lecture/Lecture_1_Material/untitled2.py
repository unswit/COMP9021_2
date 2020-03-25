# COMP9021 19T3 - Rachid Hamadi
# Quiz 4 *** Due Thursday Week 5
#
# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends
#   and around parentheses and commas, is a valid word.

word_list = []
arity_list1=[" ","_",","]
arity_list2=list(" ".join(map(chr,range(97,123))))
arity_list3=list(" ".join(map(chr,range(65,91))))

import sys
def check_symbols(n):
    for i in n:
        if i not in arity_list1+arity_list2+arity_list3:
            return False
    return True


middel_list = []
def is_valid(word, arity):



    # try:
        if arity == 0:
            return check_symbols(word)
        else:
            if word.count('(') != word.count(')') or word.count('(')==0:
                return False
            word = word.replace(',',' ')
            word = word.replace('(',' ( ')
            word = word.replace(')',' ) ')
            word = word.split()

            while len(word) > 1 :
                if word[1]=='(':
                    for i in range(len(word)):
                        if word[i] == '(':
                            left = i
                            print(i)
                        if word[i] == ')':
                            right = i
                            break
                    middel_list = word[left:right+1]
                    word = word[0:left] + word[right+1:]
                    if len(middel_list) != arity + 2:
                        return False
                else:
                    return False
            return True
    # except ValueError:
    #     return False
try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):

    print('The word is valid.')
else:

    print('The word is invalid.')

