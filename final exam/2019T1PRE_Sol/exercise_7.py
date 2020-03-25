
def sum_of_digits(input, n):
    if not input:
        if not n:
            return 1
        return 0
    if len(input) == 1 and int(input) == n:
        return 1
    if len(input) == 1 and int(input) < n:
        return 0
    left = sum_of_digits(input[1:], n - int(input[0]))
    # 2321234     4
    right = sum_of_digits(input[1:], n)
    # 2321234     5
    return left + right

def subnumbers_whose_digits_add_up_to_ext(number, sum_of_digits ,current_result, results):
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    # 123456     11 - 6 -5 == 0
    if number >= 0:
        if sum_of_digits == 0:
            results.add(current_result)
            return
    # 如果number = 2,sum of digits = 2
    if number == sum_of_digits:
        results.add(current_result * 10 + number)
        return
    # sum of digits = -1 or number == 0
    if sum_of_digits < 0 or number == 0:
        return

    a, b = divmod(number, 10)
    # a = 123,b =4
    subnumbers_whose_digits_add_up_to_ext(a, sum_of_digits - b,current_result * 10 + b,results)
    subnumbers_whose_digits_add_up_to_ext(a, sum_of_digits,current_result,results)

    # subnumbers_whose_digits_add_up_to(1234, 5)
    #               None
    # Nne                           1
    #  None, 2                  None,           2
    #   None,3  None,3           None,    3       None,   3


# POSSIBLY DEFINE OTHER


# POSSIBLY DEFINE OTHER

def subnumbers_whose_digits_add_up_to(number, sum_of_digits):
    '''
    You can assume that "number" consists of digits not equal to 0
    and that "sum_of_digits" is an integer.

    A solution is obtained by possibly deleting some digits in "number"
    (keeping the order of the remaining digits) so that the sum of
    of the remaining digits is equal to "sum_of_digits".

    The solutions are listed from smallest to largest, with no duplicate.

    >>> subnumbers_whose_digits_add_up_to(13, 2)
    []
    >>> subnumbers_whose_digits_add_up_to(222, 2)
    [2]
    >>> subnumbers_whose_digits_add_up_to(123, 6)
    [123]
    >>> subnumbers_whose_digits_add_up_to(222, 4)
    [22]
    >>> subnumbers_whose_digits_add_up_to(1234, 5)
    [14, 23]
    >>> subnumbers_whose_digits_add_up_to(12341234, 4)
    [4, 13, 22, 31, 112, 121]
    >>> subnumbers_whose_digits_add_up_to(121212, 5)
    [122, 212, 221, 1112, 1121, 1211]
    >>> subnumbers_whose_digits_add_up_to(123454321, 10)
    [145, 154, 235, 244, 253, 343, 352, 442, 451, 532, 541, 1234, 1243, \
1252, 1342, 1351, 1432, 1441, 1531, 2332, 2341, 2431, 2521, 3421, \
4321, 12331, 12421, 13321]
    '''

    results = set([])
    subnumbers_whose_digits_add_up_to_ext(int(str(number)[::-1]), sum_of_digits, 0,results)
    return sorted(results)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # print(subnumbers_whose_digits_add_up_to(123, 6))
    # print(sorted(subnumbers_whose_digits_add_up_to(123454321, 10)))
