# COMP9021 Practice 3 - Solutions

from itertools import compress

def get_all_primes(n):
    sieve = bytearray([True])*(n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i]=bytearray((n-i*i-1)//(i*2)+1)
    return ([2,*compress(range(3,n,2),sieve[1:])])

primes=get_all_primes(100_000)

a = 10000

while a < 100000:
    b=a+2
    c=b+4
    d=c+6
    e=d+8
    f=e+10
    if a in primes and b in primes and c in primes and d in primes\
       and e in primes and f in primes and primes.index(b)-1==primes.index(a)\
       and primes.index(c)-1==primes.index(b) and primes.index(d)-1==primes.index(c) \
       and primes.index(e)-1==primes.index(d) and primes.index(f)-1==primes.index(e):
        print(f'{a} {b} {c} {d} {e} {f}')
    a=a+1

