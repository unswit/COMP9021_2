# You might find the ord() function useful.

def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    You can assume that "word" is a string of
    nothing but lowercase letters.
    
    >>> longest_leftmost_sequence_of_consecutive_letters('')
    ''
    >>> longest_leftmost_sequence_of_consecutive_letters('a')
    'a'
    >>> longest_leftmost_sequence_of_consecutive_letters('zuba')
    'z'
    >>> longest_leftmost_sequence_of_consecutive_letters('ab')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('bcab')
    'bc'
    >>> longest_leftmost_sequence_of_consecutive_letters('aabbccddee')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwijlrstuvabcde')
    'rstuv'
    '''

    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    desired_length = 0
    desired_substring = ""
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

    return   desired_substring

if __name__ == '__main__':
    import doctest
    doctest.testmod()
