import sys

#n = input()
n = 3

ranks = [1,2,2]
#ranks = map(int,sys.stdin.readlines())

def get_rank(i):
    if i<0 or i > n-1:
        return 10000000
    return ranks[i]

valleys = []

for i in xrange(n):
    if get_rank(i) <= get_rank(i-1) and get_rank(i) <= get_rank(i+1) :
        valleys.append(i)

ans = [0]*n

for i in valleys:
    ans[i] = 1

    ##
    j = i-1
    cand = 2
    while j >= 0 and ranks[j]>ranks[j+1]:
        ans[j] = max(cand,ans[j])
        cand += 1
        j -= 1
        

    ##
    k = i +1
    cand = 2
    while k < n and ranks[k]>ranks[k-1]:
        ans[k] = max(cand,ans[k])
        cand += 1
        k += 1

print sum(ans)        
