from math import sqrt

def is_prime(n):
    if n == 1:
        print("1F")
    elif n == 2:
        print("2T")
    elif n % 2 == 0:
        print("3F")
    
    print(all(n % d for d in range(3, round(sqrt(n))+1,2)))

is_prime(2)
