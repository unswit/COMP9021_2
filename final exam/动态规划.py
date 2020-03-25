#python
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
    right = sum_of_digits(input[1:], n)
    left + right
    
    # return sum_of_digits(input[1:], n) + sum_of_digits(input[1:], n - int(input[0]))
sum_of_digits('1223411234242', 5)

    # a1223411234242
    #               a
    #           1           0
    #         2   0       2   0
    #       2  0 2 0    2  0 2 0
    #      3 0 30 30 30 30 30 30 30
