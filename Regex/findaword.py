# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = input()

#text = ['foo','foo-bar','(foo)']
for i in xrange(n):
    text += raw_input().split()

t = input()
#t = 1

for j in xrange(t):
    word = raw_input()
    #word = 'foo'
    
    count = 0
    
    for txt in text:
        m_obj = re.findall(r"(\w+)", txt)
        
        
        if word in m_obj:
            count += 1        
    print count
    
    
    
    
    
