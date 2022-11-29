class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort() #sort the list
        max_score = 0
        score = 0
        left = 0
        right = len(tokens)-1
        
        while left <= right:
            if tokens[left] <= power:
                score += 1
                power -= tokens[left]
                left += 1
                max_score = max(score,max_score)
                
            elif score > 0 and left < right:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                break
                
        return max_score
        