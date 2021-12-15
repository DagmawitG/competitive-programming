class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list2 = []*1
        for i in range(0,len(nums)):
            for j in range(0,len(nums)-1):
                
                if(nums[j] > nums[j+1]):
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        
        for i in range(len(nums)):
            if nums[i] == target:
                list2.append(i)
        return list2
            
            
   
            
        