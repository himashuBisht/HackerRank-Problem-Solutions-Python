
def helper(N,M):
    low = 3
    high = N+1

    while(low+1 < high):
        mid = low + (high - low)/2
        k = helper2(N,mid)
        if k < M:
            low = mid
        else:
            high = mid
    return high

def helper2(N,k):

    g1 = N%k 
    g2 = k - g1
    sz1 = N/k + 1 
    sz2 = N/k 
    ret = g1*sz1*g2*sz2 + g1*(g1-1)*sz1*sz1/2 + g2*(g2-1)*sz2*sz2/2 

    return ret 



#T = input()
T = 1

for i in xrange(T):
    #N,M = map(int,raw_input().split())
    
    N,M = 19,166



    if 2*M == N*(N-1) :
        print N
    elif 4*M<= N*N:
        print '2'
    else:
        print helper(N,M)
    
    
    
