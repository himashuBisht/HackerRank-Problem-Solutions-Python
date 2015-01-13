def nCr(n,r):
    if (r > n) or (n < 0) or (r < 0):
        return 0
    val = 1
    for j in xrange(min(r, n-r)):
        val = ((val*(n-j))//(j+1))
        val = val
    return val


print nCr(50,4)

