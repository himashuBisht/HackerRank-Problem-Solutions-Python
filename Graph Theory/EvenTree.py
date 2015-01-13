#N,M = map(int,raw_input().split())
N,M = 10,9

arr = [0]*M
#for i in xrange(M):
#    arr[i] = map(int,raw_input().split())

arr = [[2, 1], [3, 1], [4, 3], [5, 2], [6, 1], [7, 2], [8, 6], [9, 8], [10, 8]]



sol = [1]*(N+1)

for (a,b) in reversed(arr):
    sol[b] += sol[a]
    
#count number of even elements
count = -1

for c in sol:
    if c%2 == 0:
        count += 1
    
print count    

