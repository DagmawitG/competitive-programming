class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        answer = set()
        left = 0
        visited = set()
        for i in range(len(s)-9):
            temp = s[i:i+10]
           
            if temp not in visited:
                visited.add(temp)
            else:
                answer.add(temp)
        return list(answer)
                
                
            
                
        