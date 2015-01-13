A,B = 7, 8

lB = len(str(B))

setL = []
setR = []

for x in xrange(1,A+1):
    for y in xrange(1,B+1):
        L = x*y
        R = x^y
        setL += [L]
        setR += [R]
sL = set(setL)
sR = set(setR)
lL = len(sL)
lR = len(sR)

sumL = sum(sL)
sumR = sum(sR)

counter = 0

for c in sR:
    if c > (10**lB-1):
        counter += 1        
print counter
#print lB,lL,lR
#print sL
#print sR
#print sumL
#print sumR

ans = counter*sumL*(10**(lB+1)) + (lR-counter)*sumL*(10**lB) + lL*sumR

print ans



        

    
