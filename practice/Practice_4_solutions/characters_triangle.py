# COMP9021 Practice 3 - Solutions


'''
Prompts the user for a strictly positive number N
and outputs an equilateral triangle of height N.
The top of the triangle (line 1) is labeled with the letter A.
For all nonzero p < N, line p+1 of the triangle is labeled
with letters that go up in alphabetical order modulo 26
from the beginning of the line to the middle of the line,
starting with the letter that comes next in alphabetical order
modulo 26 to the letter in the middle of line p,
and then down in alphabetical order modulo 26
from the middle of the line to the end of the line.
'''


while True:
    try:
        height = int(input('Enter strictly positive number: '))
        if height <= 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again.')
#先把第一行的A的code解出来
A_code = ord('A')
#
c = A_code
# i代表行数，输出是从第一行开始逐行输出
#每一行都是先输出空格，再输出一半字母，再输出另一半字母
for i in range(1, height + 1):
    # Displays spaces on the left
    print(' ' * (height - i), end = '')
    # Displays letters before middle column
    #“_”没有任何意思，只是为了循环遍历同一行的每个元素
    #每一行的元素个数 是 行数的2倍，也就是2i
    for _ in range(1, i):
        print(chr(c), end = '')
        # Code of next letter
        c = (c - A_code + 1) % 26 + A_code
    # Displays middle column
    print(chr(c), end = '')
    # Displays letters after middle column
    for _ in range(1, i):
        # Code of previous letter
        c = (c - A_code - 1) % 26 + A_code
        print(chr(c), end = '')
    print()
    # Code of first letter to be input on next line
    #第二行开头字母为C，C的code =A_code + 1
    #第三行开头字母为D，D_code = A_code +1 + 2
    # 第四行开头字母G，G_code = A_code+1+2+3
    #第i行开头字母的code = A_code+1+2...+(n-1)
    #用等差数列公式 =A_code + (1+(n-1)*(n-)/2=A_code+n*(n-1)/2
    c = ((1 + i) * i // 2) % 26 + A_code
