N = 8
A = [1,1,4,7]
B = [10,3,6,10]
    #!/bin/python


inputintvls = [(5,7),(6,7),(3,4),(1,7),(1,2),(4,5),(1,6),(4,5)]

test = 1

# code snippet for illustrating input/output

#test = int(raw_input())

for t in range(0, test):
    #N = int(raw_input())
    
    #inputintvls = []
    #for i in xrange(N):
    #    inputintvls.append([int(x) for x in raw_input().split(' ')])

    inputintvls = sorted(inputintvls)
    
    cutIntvls   = []
    passedList  = []
    
    def getOverlap(a, b):
        return(max(a[0], b[0]),min(a[1], b[1]))

    def check3cut(d):
        
        for i in xrange(len(cutIntvls)):
            k,r = getOverlap(cutIntvls[i][0],d)
            if k > r:
                pass
            else:
                # remove the one with the largest ending time
                # also remove it from the passed list
                
                
                if d[1] >= max(cutIntvls[i][1][1],cutIntvls[i][2][1]):
                    pass
                else:                    
                    if cutIntvls[i][1][1] >= cutIntvls[i][2][1]:
                        passedList.remove(cutIntvls[i][1])                        
                        temp1 = cutIntvls[i][1]
                    else:
                        passedList.remove(cutIntvls[i][2])
                        temp1 = cutIntvls[i][2]
                    temp = cutIntvls[:]
                    #print "temp",temp
                    for c in temp:
                        #print "c:",c[1:],"temp1:",temp1
                        if temp1 in c[1:] :
                            cutIntvls.remove(c)
                    #print "temp",temp        
                    #print "cut intvls",cutIntvls
                    updateCutIntvls(d)
                    passedList.append(d)                        
                    
                return True
        return False
    
        
    def updateCutIntvls(d):
        #global cutIntvls
        for c in passedList:
            k,r = getOverlap(c,d)
            if k > r:
                pass
            else:
                cutIntvls.append(((k,r),c,d))
    
    for j in xrange(N):
        newIntvl = inputintvls[j]
        #print "newIntvl:",newIntvl,
        c3c = check3cut(newIntvl)
        #print "c3c:",c3c
        if c3c:
            # remove the one with the largest ending time            
            pass
        else:        
            updateCutIntvls(newIntvl)
            passedList.append(newIntvl)
        #print "passedList:",passedList,
        #print "cutIntvls",cutIntvls,
        #print ""
    #print passedList
    print len(passedList)

    


