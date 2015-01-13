#Author : Khaleeque Ansari

t = input()
for i in xrange(t):
    n = input()       
    shr = map(int,raw_input().split())    
    ans  = 0    
    locmax = shr[n-1]        
    
    for i in range(n-2,-1,-1):
        if shr[i] < locmax:
            ans += locmax - shr[i]
        else:
            locmax = shr[i]
    print ans