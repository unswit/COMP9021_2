# COMP9021 Practice 3 - Solutions


'''
Prompts the user for a number N and prints out the first N + 1 lines of Pascal triangle.
'''


while True:
    try:
        N = int(input('Enter a nonnegative integer: '))
        if N < 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again')
        



        
#先将同一行出现的数字都以值为1显示，打印成列表的形式，列表中再套子列表，每个子列表代表同一行出现的数字。
#一共有N+1个子列表
pascal_triangle = [[1]*(n+1) for n in range(N+1)]

#先for每个子列表遍历
for n in range(2,N+1):
    #针对某一行中将其中前一半的1换成正确的数字
    for k in range(1,n//2+1):
        #列表中第n个子列表中的第k个元素，等于前一个子列表[n-1]中第[k-1]个元素和第[k]个元素之和
        pascal_triangle[n][k]=pascal_triangle[n-1][k-1]+pascal_triangle[n-1][k]
    #某一行中将其中后一半的1换成正确的数字
    for k in range(1,(n+1)//2):
        #第n个子列表中的第[n-k]个元素等于同一个子列表中第[n]个元素
        pascal_triangle[n][n-k]=pascal_triangle[n][k]
#最后来找空格个数
#最长的数字一定在最后一个子列表[N]中，最长的数在最中间
wight =len(str(pascal_triangle[N][N//2]))

#开始打印列表，n代表第n个子列表，所以逐个打印子列表
for n in range(N+1):
    #先打印空格,空格个数
    print(' '*wight*(N-n),end='')
    #再打印子列表
    #:d代表格式化.
    #:{weigh}表示缩进的格数
    # 在子列表中遍历逐个打印k，并且每个k前要有长度为wight的空格
    print((' '*wight).join(f'{pascal_triangle[n][k]:{wight}d}'for k in range(n+1)))
