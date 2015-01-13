inpStr = 'aaabbbb'


s = sorted(inpStr)

stop = 0
i = 0
l =len(s)
printed = 0
while stop !=2 and i < l-1:
    c1 = s[i]
    c2 = s[i+1]

    if c1 == c2:
        i +=2
        pass
    else:
        i +=1
        stop +=1
    if stop == 2:
        print 'NO'
        printed = 1
        break

if printed == 0:
    if l-i + stop == 2:
        print 'NO'
    else:   
        print 'YES'

    
