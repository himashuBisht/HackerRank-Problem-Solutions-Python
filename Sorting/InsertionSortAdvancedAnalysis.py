#T = input()
T = 1
for i in xrange(T):
    #N = input()    
    
    #arr = map(int,raw_input().split())
    #arr = [4, 1, 1, 2, 3, 1]
    #arr = [1, 3, 5, 2, 4]
    #ss = '62935 82200 877141 585771 619073 183328 809452 189197 41883 777611 360495 295099 198393 308583 537954 11054 515803 403848'
    #ss = '4 1 5 9 2 8 6 3 7'
    #arr = map(int,ss.split())
    N = len(arr)
        
    
    def merge_and_count(a, b):
        assert a == sorted(a) and b == sorted(b)
        c = []
        count = 0
        i, j = 0, 0
        while i < len(a) and j < len(b):
            c.append(min(b[j], a[i]))
            if b[j] < a[i]:
                count += len(a) - i # number of elements remaining in `a`
                j+=1
            else:
                i+=1
        # now we reached the end of one the lists
        c += a[i:] + b[j:] # append the remainder of the list to C
        return count, c

    def sort_and_count(L):
        if len(L) == 1: return 0, L
        n = len(L) // 2 
        a, b = L[:n], L[n:]
        ra, a = sort_and_count(a)
        rb, b = sort_and_count(b)
        r, L = merge_and_count(a, b)
        return ra+rb+r, L

    a,b = sort_and_count(arr)
    print a 
