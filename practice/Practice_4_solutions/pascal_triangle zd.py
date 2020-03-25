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

pascal_triangle = [[1]*(n+1) for n in range(0,N+1)]

        
for n in range(N+1):
    for k in range(1,n):
        pascal_triangle[n][k]=pascal_triangle[n-1][k-1]+pascal_triangle[n-1][k]

#for i in range(N+1):
weight = len(str(pascal_triangle[N][N//2]))

for n in range(N+1):
    print(' '*weight*(N-n),end='')
    print((' '*weight).join(f'{pascal_triangle[n][k]:{weight}d}'for k in range(n+1)))
    
