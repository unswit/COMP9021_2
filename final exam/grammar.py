from itertools import compress
def get_primes_3(n):
    sieve = bytearray([True]) * (n//2)
    for i in range(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n - i*i-1)//(2*i)+1)
    print([2, *compress(range(3,n,2),sieve[1:])])
get_primes_3(15)
