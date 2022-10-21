class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp_helper(ptr1,ptr2):
            ans = 0
            if ptr1 == len(text1) or ptr2 == len(text2):
                return 0
            if text1[ptr1] == text2[ptr2]:
                ans = 1 + dp_helper(ptr1+1,ptr2+1)
                return ans
                
           
            case1 =  dp_helper(ptr1+1,ptr2)
            case2 =  dp_helper(ptr1,ptr2+1)
            return max(case1,case2)
       
        return dp_helper(0,0)
        
        
                
                
                
            
       
        
        