import sys
from math import factorial

def f(n):
    '''
    >>> f(0)
    0 factorial is 1
    The last nonzero digit in 0 factorial is 1
    >>> f(2)
    2 factorial is 2
    The last nonzero digit in 2 factorial is 2
    >>> f(4)
    4 factorial is 24
    The last nonzero digit in 4 factorial is 4
    >>> f(10)
    10 factorial is 3628800
    The last nonzero digit in 10 factorial is 8
    >>> f(20)
    20 factorial is 2432902008176640000
    The last nonzero digit in 20 factorial is 4
    >>> f(30)
    30 factorial is 265252859812191058636308480000000
    The last nonzero digit in 30 factorial is 8
    >>> f(40)
    40 factorial is 815915283247897734345611269596115894272000000000
    The last nonzero digit in 40 factorial is 2
    '''

    n_factorial=str(factorial(n)).strip('0')
    print(f'{n} factorial is {factorial(n)}')
    print(f"The last nonzero digit in {n} factorial is {n_factorial[-1]}")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
