class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda word: len(word))
        dictionary = {word: 1 for word in words}
        result = 1 
        
        for word in words:
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in dictionary:
                    dictionary[word] = max(1 + dictionary[prev], dictionary[word])
                    result  = max(result , dictionary[word])
        
        return result 
        