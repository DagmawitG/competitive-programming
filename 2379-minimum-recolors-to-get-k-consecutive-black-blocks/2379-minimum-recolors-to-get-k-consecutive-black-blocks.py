class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = k - 1
        frequency = Counter(blocks[left:right+1])
        minValue = frequency['W']
        if k == len(blocks):
            return frequency['W']
        else:
            left += 1
            right += 1
            while left <= right and right < len(blocks):
                frequency = Counter(blocks[left:right+1])
                if 'W' in frequency:
                    minValue = min(minValue, frequency['W'])
                else:
                    return 0
                
                left += 1
                right += 1
        return minValue
                
                
            
            
                
         