class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        answer = set()
        left = 0
        visited = set()
        for i in range(len(s)-9):
            right = i 
            count = 0
            temp = ''
            while count < 10 and right < len(s):
                temp += s[right]
                right += 1
                count += 1
            if temp not in visited:
                visited.add(temp)
            else:
                answer.add(temp)
        return list(answer)
                
                
            
                
        