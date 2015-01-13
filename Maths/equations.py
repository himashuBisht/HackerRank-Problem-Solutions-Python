# prime numbers are only divisible by unity and themselves
# (1 is not considered a prime number by convention)
def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
# test ...

import math

n = 2

pl = [2]


for i in xrange(1,n/2 + 1):
    j = 2*i + 1
    if isprime(j):
        pl += [j]
lenth = len(pl)

#print pl
for i in xrange(lenth):
    num = n
    count = 0
    divsor = pl[i]
    while num >= divsor:
        count += (num/divsor)
        num /= divsor
    pl[i] = count
#print pl    
pl = map(lambda x: x * 2 + 1, pl)


p = 1
for i in pl:
    p *= i

print p%1000007
    


    
