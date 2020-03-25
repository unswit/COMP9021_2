import sys
from itertools import compress
from itertools import sqrt
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    else:
        return (n % d for d in range(3,round(sqrt(n))+1,2))


def f(a, b):
    '''
    The prime numbers between 2 and 12 (both included) are: 2, 3, 5, 7, 11
    The gaps between successive primes are: 0, 1, 1, 3.
    Hence the maximum gap is 3.
    
    Won't be tested for b greater than 10_000_000
    
    >>> f(3, 3)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 4)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 5)
    The maximum gap between successive prime numbers in that interval is 1
    >>> f(2, 12)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(5, 23)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(20, 106)
    The maximum gap between successive prime numbers in that interval is 7
    >>> f(31, 291)
    The maximum gap between successive prime numbers in that interval is 13
    '''
    if a <= 0 or b < a:
        sys.exit()
    max_gap = 0
    # Insert your code here
    
    
    for number in range(a,b+1):
        if is_number

    

    
    if b_prime:
        first  = b_prime[0]
        for second in b_prime[1:]:
            gap = second -first
            if gap > max_gap:
                max_gap = gap
            first = second
    print(b_prime)
    print(f'The maximum gap between successive prime numbers in that interval is {max_gap}')
    


if __name__ == '__main__':
    import doctest
    doctest.testmod()
 
