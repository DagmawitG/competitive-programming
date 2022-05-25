class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        res = []
        envelopes = sorted(envelopes,key= lambda x:(x[0],-x[1]))
        for w,h in envelopes:
            # i,n = 0,len(res)
            # while i<n:
            #     if h <= res[i]:
            #         break
            #     i+=1
            i = bisect_left(res,h)
            if i == len(res):
                res.append(h)
            else:
                res[i]=h
            
            
        return len(res)
      

                
                
                
                
        
        
        