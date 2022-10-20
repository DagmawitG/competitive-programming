class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left = i + 1
            right = len(nums)-1
            while(left < right):
                summ = nums[i]+ nums[left]+nums[right]
                if summ > 0:
                    right -= 1
                elif summ < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result
                
                    
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        Use the two sum problem for this solution
        '''
        
#         mapping = {}
#         result = []
#         n = len(nums)
#         for i in range(n-2):
            
#             index = i + 1
#             while index < n:
#                 difference = 0 - (nums[i]+nums[index])
#                 if difference in mapping and (i !=mapping[difference]) :
#                     result.append((nums[i],difference,nums[index]))
#                     print(result) 
#                 mapping[nums[index]] = index
#                 index += 1
        
        
#         print(result)
                    
        