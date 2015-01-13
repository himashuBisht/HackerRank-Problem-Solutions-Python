
#T = input()
T = 1

permtable = {}

def strictly_inc(perm):
    for i in range(len(perm)-1):                
        if perm[i]>perm[i+1]:            
            return False
    return True
        
def strictly_dec(perm):
    for i in xrange(len(perm)-1):
        if perm[i]<perm[i+1]:
            return False
    return True
    

def helper(perm,n,alice_turn):
    bob_turn = not alice_turn

    perm_s = str(perm)[1:-1]

    if perm_s in permtable:
        return permtable[perm_s]

    #when 3 elem in list
    if n == 3:
        if strictly_inc(perm) or strictly_dec(perm):
            return bob_turn
        else:
            return alice_turn

    #strictly increasing seq
    elif strictly_inc(perm):
        permtable[perm_s] = bob_turn
        return bob_turn

    #strictly decreasing seq
    elif strictly_dec (perm):
        if n%2 == 0:
            permtable[perm_s] = alice_turn
            return alice_turn
        else:
            permtable[perm_s] = bob_turn
            return bob_turn
        

    #otherwise check after removing one by one element & if any
    #config. makes Alice win push it in permtable and return True
    else:
        for c in perm:
            t_perm = list(perm)
            perm.remove(c)
            

            k = helper(t_perm,n-1,bob_turn)

            if alice_turn and k:
                permtable[perm_s] = True
                return True
            elif bob_turn and (not k):
                permtable[perm_s] = False
                return False
                
        permtable[perm_s] = bob_turn
        return bob_turn
            
                



    


for i in xrange(T):
    #N = input()
    N = 3

    #arr = map(int,raw_input().split())
    arr = [3,2,1,4]


    if (len(arr) == 2) or helper(arr,N,True) :
        print 'Alice'
    else:
        print 'Bob'

    #flushing for next test case
    permtable = {}
