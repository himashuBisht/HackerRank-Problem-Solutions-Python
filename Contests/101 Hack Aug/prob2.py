# Enter your code here. Read input from STDIN. Print output to STDOUT
#arr = raw_input()
arr = 'cabacbccbb'
tarr = list(reversed(arr))
arr = sorted(arr)
t = arr[::2]

dict = [0]*26

for c in t:
    dict[ord(c)-97] += 1

old = dict[:]
helper = [1]*len(t)
ans = []

count = 0
temp = t[0]

for c in tarr :
    dict[ord(c)-97] -= 1
    if len(ans) == len(t):
        break
    if c == temp:
        ans.append(c)
        helper[count] = 0

        while(helper[count] == 0 and  count < len(t) - 1):
            count += 1
            temp = t[count]
            
    elif dict[ord(c)-97] < 0  :
        if ans.count(c) == old[ord(c)-97]:            
            pass
        else:
            ans.append(c)
            helper[count] = 0

l = ''            
for c in ans:
    l += c

print l    
