class Solution(object):
    def sortColors(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(arr)
        frequency = [0]*300
        for i in range(l):
            frequency[arr[i]] += 1
        ptr = 0
        for j in range(len(frequency)):
            count = frequency[j]
            while(count):
                arr[ptr] = j
                ptr+=1
                count-=1
        return arr
            