from math import factorial

inpStr = 'cdcdcdcdeeeef'

s = sorted(inpStr)


i = 0
l =len(s)

char_list = []
while i < l-1:
    if s[i] == s[i+1]:        
        char_list += s[i]
        i +=2
    else:
        i +=1

a = char_list
ll = len(a)
#print a
temp=a[0]
cnt=0
b=[]
for i in range(ll):
    if(a[i] == temp):
        cnt+=1
    else:
        b.append(cnt)
        cnt=1
        temp=a[i]

b.append(cnt)

denom = 1
for n in b:
    denom *= factorial(n)
numr = factorial(ll)

ans = numr/denom

ans %=(10**9 + 7)
print ans


