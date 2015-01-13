stop = False
    ans = 0
    prev = 0
    curr = 0
    
    while not stop:#stop when decreasing sequence or only one element left
        
        def get_shr_pric(i):
        if i < 0 or i > n-1:
            return 0
        return shr[i]
           
        #find  peaks 
        peaks = []
        for j in xrange(n):
            if get_shr_pric(j) >= get_shr_pric(j-1) and get_shr_pric(j) > get_shr_pric(j+1):
                peaks.append(j)
            
            
            
        
        curr = peaks.index(max(shr[prev:]))
        s = 0
        for n in xrange(prev,curr):
            s += shr[n]
        ans += (curr - prev)*shr[curr] - s                
        
        prev = curr + 1
        if (shr[prev:]) == sorted((shr[prev:]),reverse=True):
            stop = True
        
        inc_peaks = []
        l = len(peaks)
    
        if l > 1:
            for k in xrange(l-1):
                if shr[peaks[k]] > shr[peaks[k+1]]:
                    inc_peaks.append(peaks[k])
            inc_peaks.append(peaks[l-1])
        else:
            inc_peaks = peaks
        
            
        
        
    print ans
        
        
        
    
        
