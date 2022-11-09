class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        
        def recursion(index,string):
            if index == len(s):
                eachPossible = ''.join(string)
                result.append(eachPossible)
                return
            if s[index].isalpha():
                swapped = [s[index].swapcase()]
                recursion(index+1,string + swapped)
            
            recursion(index+1,string+[s[index]])
            
        recursion(0,[])
        return result
                
        