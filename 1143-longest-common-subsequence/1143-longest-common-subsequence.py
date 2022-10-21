class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1]*(len(text1)+1) for i in range(len(text2)+1)]
        print(memo)
        def dp_helper(ptr1,ptr2):
            ans = 0
            if ptr1 == len(text1) or ptr2 == len(text2):
                return 0
            if memo[ptr2][ptr1] != -1:
                return memo[ptr2][ptr1]
            if text1[ptr1] == text2[ptr2]:
                ans = 1 + dp_helper(ptr1+1,ptr2+1)
                memo[ptr2][ptr1] = ans
                return memo[ptr2][ptr1]
                
           
            case1 =  dp_helper(ptr1+1,ptr2)
            case2 =  dp_helper(ptr1,ptr2+1)
            memo[ptr2][ptr1] = max(case1,case2)
            return memo[ptr2][ptr1]
       
        return dp_helper(0,0)
        
        
                
                
                
            
       
        
        