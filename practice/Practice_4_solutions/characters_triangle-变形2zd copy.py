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

A_code = ord("A")
c=A_code

for i in range(1,height+1):
    print(" " * (height-i),end="")
    if i %2 ==0:
        for _ in range(1,i*2-1):
            print(chr(c),end='')
            c = (c-A_code+1)%26 +A_code
        print(chr(c),end='')
    else:
        for _ in range(1,i*2-1):
            print(chr(c),end='')
            c = (c-1-A_code)%26 +A_code
        print(chr(c),end='')
    print()
    if i%2 ==0:
        c = (c-2*i)%26 + A_code
    else:
        c = (i*(i+1)//2)%26 + A_code
 
        
    
    
    
    
            
 

    

