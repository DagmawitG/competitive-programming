class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        s=set(nums)
        d={}
        for i in s:
            d[i]=nums.count(i)
        maxc=max(d.values())
        re=nums[::-1]
        res=9999999999
        for key,value in d.items():
            if value==maxc:
                res=min(res,len(nums)-nums.index(key)-re.index(key))
        return res
        