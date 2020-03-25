

def f(word):
    '''
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('xy')
    The longest substring of consecutive letters has a length of 2.
    The leftmost such substring is xy.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    desired_length = 0
    desired_substring = ''
    # Insert your code here
    if word:
        first = word[0]
        letters = [first]
        # 套路
        for second in word[1:]:
            if ord(first) + 1 == ord(second):
                letters[-1] +=second
            else:
                # desired_length = max(desired_length,len(letters[-1]))
                letters.append(second)

            first = second
        #
        for letter in letters:
            if desired_length < len(letter):
                desired_length = len(letter)

        for letter in letters:
            if desired_length == len(letter):
                desired_substring = letter
                break

    print(f'The longest substring of consecutive letters has a length of {desired_length}.')
    print(f'The leftmost such substring is {desired_substring}.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
