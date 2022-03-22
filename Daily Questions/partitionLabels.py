class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        result = []
        start = 0
        end = 0
      
        for i in range(len(s)):
            end = max(end,s.rfind(s[i])) 
            if i == end :
                result.append(end+1 - start)
                start = end + 1
                
        return result         
                    
                    
                    
                    
                    
                
                
                
        