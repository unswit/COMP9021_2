from itertools import compress
from math import sqrt
from collections import Counter
from collections import defaultdict

def get_prime(n):
    sieve = bytearray([True]*(n//2))
    for i in range(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i]=bytearray((n-i*i-1)//(2*i)+1)
    return [2,*compress(range(3,n,2),sieve[1:])]


primes = get_prime(7)
print(primes)




def get_divisor(n):
    if n==1:
        return [1]
    result = []
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            result.append(i)
            result.append(n//i)
    return result

divisors= get_divisor(88)
print(divisors)

list=[1,2,3,4,5,2,34,5,3,3,2]

dic=defaultdict(int)
for i in list:
    dic[i]=list.count(i)

print(dic)


with open("a.txt","r") as read_file:
    lines = read_file.readlines()
print(lines)

     
