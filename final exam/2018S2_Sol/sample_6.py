'''
is_valid_prefix_expression(expression) checks whether the string expression
represents a correct infix expression (where arguments follow operators).

evaluate_prefix_expression(expression) returns the result of evaluating expression.

For expression to be syntactically correct:
- arguments have to represent integers, that is, tokens that can be converted to an integer
  thanks to int();
- operators have to be any of +, -, * and /;
- at least one space has to separate two consecutive tokens.

Assume that evaluate_prefix_expression() is only called on syntactically correct expressions,
and that / (true division) is applied to a denominator that is not 0.

You might find the reversed() function, the split() string method,
and the pop() and append() list methods useful.
'''

from operator import add, sub, mul, truediv


class ListNonEmpty(Exception):
    pass


def is_valid_prefix_expression(expression):
    '''
    >>> is_valid_prefix_expression('12')
    Correct prefix expression
    >>> is_valid_prefix_expression('+ 12 4')
    Correct prefix expression
    >>> is_valid_prefix_expression('- + 12 4 10')
    Correct prefix expression
    >>> is_valid_prefix_expression('+ - + 12 4 10 * 11 4')
    Correct prefix expression
    >>> is_valid_prefix_expression('/ + - + 12 4 10 * 11 4 5')
    Correct prefix expression
    >>> is_valid_prefix_expression('+ / + - + 12 4 10 * 11 4 5 - 80 82 ')
    Correct prefix expression
    >>> is_valid_prefix_expression('twelve')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('2 3')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ + 2 3')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+1 2')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ / 1 2 *3 4')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+1 2')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ +1 2')
    Correct prefix expression
    >>> is_valid_prefix_expression('++1 2')
    Incorrect prefix expression
    >>> is_valid_prefix_expression('+ +1 -2')
    Correct prefix expression
    '''
    stack = []
    #一个try至少带一个except
    try:
        #将运算符号换成python能看懂的语言
        operators = {'+': add, '-': sub, '*': mul, '/': truediv}
        #需要从后往前遍历，所以先把expression翻
        #注意⚠️用完reversed返回的是迭代器的形式<list_reverseiterator object at 0x11229e8d0>
        #假如需要输出一个能看懂的list，前面需要加个表list(expression)
        expression = reversed([x for x in expression.split()])
        #开始遍历～～
        for x in expression:
            #先检查x是数字还是运算符
            #看一看x有没有在operator中出现
            #如果是运算符，就要开始进行运算了，再将运算结果仍到stack中
            if x in operators:
                #先取出需要进行运算的两个数字
                #pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
                left = stack.pop()
                right = stack.pop()
                #operators[x]定位运算符的python表达式
                #(left，rihgt)需要运算的两个数，运算完结果放入stack
                stack.append(operators[x](left, right))
            else:
                #如果是数字，直接往stack中仍
                stack.append(int(x))
        # only one left
        if len(stack) > 1:
            #Python）异常处理try...except、raise
            #异常的话，像是IndexError, ValueError,都要用raise返回
            raise ListNonEmpty()

    # Replace pass above with your code
    # - IndexError is raised in particular when trying to pop from an empty list
    # - ValueError is raised in particular when trying to convert to an int
    #   a string that cannot be converted to an int
    # - ListNonEmpty is expected to be raised when a list is found out not to be empty
    except (IndexError, ValueError, ListNonEmpty):
        print('Incorrect prefix expression')
    else:
        print('Correct prefix expression')


def evaluate_prefix_expression(expression):
    '''
    >>> evaluate_prefix_expression('12')
    12
    >>> evaluate_prefix_expression('+ 12 4')
    16
    >>> evaluate_prefix_expression('- + 12 4 10')
    6
    >>> evaluate_prefix_expression('+ - + 12 4 10 * 11 4')
    50
    >>> evaluate_prefix_expression('/ + - + 12 4 10 * 11 4 5')
    10.0
    >>> evaluate_prefix_expression('+ / + - + 12 4 10 * 11 4 5 - 80 82 ')
    8.0
    >>> evaluate_prefix_expression('+ +1 2')
    3
    >>> evaluate_prefix_expression('+ +1 -2')
    -1
    '''
    # Insert your code here
    stack = []

    #将运算符号换成python能看懂的语言
    operators = {'+': add, '-': sub, '*': mul, '/': truediv}
    #需要从后往前遍历，所以先把expression翻
    #注意⚠️用完reversed返回的是迭代器的形式<list_reverseiterator object at 0x11229e8d0>
    #假如需要输出一个能看懂的list，前面需要加个表list(expression)
    expression = reversed([x for x in expression.split()])
    for x in expression:
        if x in operators:
            left = stack.pop()
            right = stack.pop()
            stack.append(operators[x](left, right))
        else:
            stack.append(int(x))
    # only one left
    if len(stack) == 1:
        print(stack[0])

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    # evaluate_prefix_expression('+ 12 4')
