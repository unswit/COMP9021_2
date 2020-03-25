import sys
from math import sqrt

def get_all_divisor(n):
    if n==1:
        return 1
    result=[]
    for i in range(2,int(sqrt(n))+1):
        if n % i ==0:
            result.append(i)
            result.append(n // i)
    return result


try:
    N = int(input('Input an integer: '))
except ValueError:
    print('Incorrect imput, giving up.')
    sys.exit()

for n in range(2,N+1):
    if 1+sum(i for i in range(2,n//2 +1) if n % i==0)==n:
        print(n, 'is a perfect number.')
