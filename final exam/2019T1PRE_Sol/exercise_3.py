from itertools import compress, accumulate
from math import sqrt
import operator


def get_primes_3(n):
    """ Returns  a list of primes < n for n > 2 """
    if n < 2:
        return []
    if n == 2:
        return [2]
    sieve = bytearray([True]) * (n // 2)

    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = bytearray((n - i * i - 1) // (2 * i) + 1)

    return [2, *compress(range(3, n, 2), sieve[1:])]


def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    # Only used to test odd numbers.
    return all(n % d for d in range(3, round(sqrt(n)) + 1, 2))


def second_method(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        # 其实也就是用前几个prime，所以这里直接取10000以下的所有primes而不是用numbr
        primes = get_primes_3(10000)

        m = number
        results = set([])
        for prime in primes:
            while m != 0 and m != 1:
                a, b = divmod(m, prime)
                if b == 0:
                    results.add(prime)
                    m = a
                else:
                    break
            else:
                break

        return list(accumulate(results, func=operator.mul))[-1]


def first_method(number):
    m = number
    result = []
    factor = 2
    while m > 1 and factor <= number:
        if is_prime(factor) and m % factor == 0:
            result.append(factor)
            m = m // factor
            while m % factor == 0:
                m = m // factor
        factor += 1

    result = list(set(result))
    if result:
        total = result[0]
        for item in result[1:]:
            total *=item
        return total



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
    # 11111111111111* 111111111111 =
    return second_method(number)
    # second_method(number)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    # single_factors(154)
