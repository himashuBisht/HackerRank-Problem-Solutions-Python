
#change_base
def change_base(n,base):
    digits = []
    while(n != 0):
        digits.append( n%base)
        n /= base    
    return digits




#T = input()
T = 1

for i in xrange(T):
    #n,P = map(int,raw_input().split())
    n,P = 3,2

    pbase = change_base(n,P)

    prod = 1
    for x in pbase:
        prod *= (x+1)
    print (n+1-prod)
        

    

    
