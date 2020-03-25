# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def rectangle(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.
    
    >>> rectangle(1, 1)
    a
    >>> rectangle(2, 3)
    ab
    dc
    ef
    >>> rectangle(3, 2)
    abc
    fed
    >>> rectangle(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    first = ord('a')
    count = 0
    for row in range(0, height):
        line = ''
        for column in range(0, width):
            line += chr(first + count % 26)
            count += 1

        if row % 2 == 0:
            print(line)
        else:
            print(line[::-1])


if __name__ == '__main__':
    import doctest

    doctest.testmod()
