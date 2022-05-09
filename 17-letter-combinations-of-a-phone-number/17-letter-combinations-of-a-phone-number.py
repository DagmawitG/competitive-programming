class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        mapping = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",  
        }
      
        for i in range(len(digits)):
            temp = []
            if len(result) == 0:
                result = mapping[digits[i]]
                continue
            for j in mapping[digits[i]]:
                for res in result:
                    temp.append(res+j)
            result = temp
        return result
        
        