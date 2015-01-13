# Enter your code here. Read input from STDIN. Print output to STDOUT
#T = input()
T = 1

for i in xrange(T):
    #n,k = map(int,raw_input().split())
    n,k = 4,5
    A = []
    B = []
    #A = map(int,raw_input().split())
    A = [1,2,2,1]
    A = sorted(A)
    #B = map(int,raw_input().split())
    B = [3,3,3,4]
    B = sorted(B)

    Run = True
    
    for i in xrange(n):
        if A[i] + B[n-i-1] < k:
            Run = False
            break
        
    if Run :
        print'YES'
    else:
        print 'NO'
