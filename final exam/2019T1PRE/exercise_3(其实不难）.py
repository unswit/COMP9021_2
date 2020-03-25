from itertools import compress, accumulate
from math import sqrt
from collections import defaultdict
import operator

def get_all_primes(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    sieve = bytearray([True]) * (n // 2)

    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i // 2]:
             sieve[i * i // 2::i] = bytearray((n - i * i - 1) // (2 * i) + 1)
    return [2,*compress(range(3, n, 2), sieve[1:])]
                   


def single_factors(number):
    '''
    Returns the product of the prime divisors of "number"
    (using each prime divisor only once).

    You can assume that "number" is an integer at least equal to 2.

    >>> single_factors(2)
    2
    >>> single_factors(4096)                 # 4096 == 2**12
    2
    >>> single_factors(85)                   # 85 == 5 * 17
    85
    >>> single_factors(10440125)             # 10440125 == 5**3 * 17**4
    85
    >>> single_factors(154)                  # 154 == 2 * 7 * 11
    154
    >>> single_factors(52399401037149926144) # 52399401037149926144 == 2**8 * 7**2 * 11**15
    154
    '''
    # return 0
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    # return
    primes=get_all_primes(10000)
    result = set([])
    if number ==1:
        return 1
    if number==2:
        return 2
    else:
        m =number
        for i in primes:
            while m!=0 and m!=1:
                a,b = divmod(m,i)
                if b==0:
                    result.add(i)
                    m =a
                else:
                    break
            else:
                break
        return list(accumulate(result, func=operator.mul))[-1]
            

    

    
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
