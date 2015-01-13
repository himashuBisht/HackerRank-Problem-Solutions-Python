#Enter your code here. Read input from STDIN. Print output to STDOUT
import math
from decimal import *


mod = 0

def firstKdigits(n,k):
    getcontext().prec = 40
    nlog2 = n*Decimal('0.301029995663981195213738894724493026768189881462108541310427')
    f = Decimal(nlog2) - Decimal(int(nlog2))
    z = Decimal(f + k - 1)
    ans = Decimal(10**z)
    return int(ans)
           
def lastKdigits(k):        
    if k == 0:
        return 1
    
    t = lastKdigits(k/2)
    
    if k%2:
        return((2*t%mod)*t)%mod
    else:
        return (t*t)%mod


#t = input()
t = 1

for i in range(9,0,-1):
    #a,k = map(int,raw_input().split())
    
    a =10**i
    k = 9
    
    f = firstKdigits(a-1,k)
    mod = 10**k
    l = lastKdigits(a-1)
    ans  = f+l
    print ans     
