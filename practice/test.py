import sys


def check_increasing(n):
    m = str(n)
    if m:
        first = m[0]
        for second in m[1:]:
            if first >= second:
                return False
            second = first
        return True
    else:
        return False


def check_decreasing(n):
    m = str(n)
    if m:
        first = m[0]
        for second in m[1:]:
            if first <= second:
                return False
            second = first
        return True
    else:
        return False


def f(a, b):
    '''
    Finds all numbers i and j with a <= i <= j <= b such that:
    - i + j is even;
    - when read from left to right, the digits in i are strictly increasing
    - when read from left to def is_ prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    return all(n % d for d in range(3, round(sqrt(n))+1,2)right, the digits in j are strictly decreasing
    - when read from left to right, the digits in the average of i and j are
      either strictly increasing or strictly decreasing

    Outputs the solutions from smallest i to largest i,
    and for a given i from smallest j to largest j.

    >>> f(10, 20)
    12 and 20 with 16 as average
    14 and 20 with 17 as average
    16 and 20 with 18 as average
    18 and 20 with 19 as average
    >>> f(30, 50)
    34 and 40 with 37 as average
    34 and 42 with 38 as average
    34 and 50 with 42 as average
    35 and 41 with 38 as average
    35 and 43 with 39 as average
    36 and 40 with 38 as average
    36 and 42 with 39 as average
    36 and 50 with 43 as average
    37 and 41 with 39 as average
    37 and 43 with 40 as average
    38 and 40 with 39 as average
    38 and 42 with 40 as average
    39 and 41 with 40 as average
    39 and 43 with 41 as average
    46 and 50 with 48 as average
    48 and 50 with 49 as average
    >>> f(400, 700)
    456 and 630 with 543 as average
    457 and 521 with 489 as average
    458 and 520 with 489 as average
    459 and 621 with 540 as average
    468 and 510 with 489 as average
    478 and 542 with 510 as average
    479 and 541 with 510 as average
    489 and 531 with 510 as average
    567 and 653 with 610 as average
    568 and 610 with 589 as average
    568 and 652 with 610 as average
    569 and 651 with 610 as average
    578 and 642 with 610 as average
    579 and 641 with 610 as average
    589 and 631 with 610 as average
    589 and 651 with 620 as average
    589 and 653 with 621 as average
    '''

    for i in range(a, b + 1):
        if check_increasing(i):
            for j in range(i + 1, b + 1):
                if check_decreasing(j):
                    average, c = divmod((i + j), 2)
                    if c == 0 and (check_increasing(average)
                                   or check_decreasing(average)):
                        print(f'{i} and {j} with {average} as average')


if __name__ == '__main__':
    import doctest

    doctest.testmod()
