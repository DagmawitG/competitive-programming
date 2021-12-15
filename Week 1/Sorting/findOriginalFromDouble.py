class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        l = len(changed)
        if l % 2:
            return []
        
        list1 = [] 
        c = Counter(changed)
        changed.sort()
        for value in changed:
            if (value == 0 and c[value] >= 2): 
                c[value] -= 2
                
                list1.append(value)
            elif(value > 0 and c[value] and c[value * 2]):
                c[value] -= 1
                c[value*2] -= 1
                list1.append(value)
                
            
            
        if len(changed)//2 == len(list1):
            return list1
        