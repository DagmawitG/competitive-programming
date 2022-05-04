class Node:
    def __init__(self):
        self.children = [None]*26
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = Node()
        self.result = ""
    def insert(self, word: str) -> None:
        count = 0
        current = self.root
        for char in word:
            index = ord(char)-ord('a')
            if  current.children[index] is None:
                
                current.children[index] = Node()
            if current.isWord:
                count += 1
                
            current = current.children[index]
        current.isWord = True 
        if count == len(word)-1:
            temp = word
            if len(temp)> len(self.result):
                self.result = temp
        
    def getResult(self):
        return self.result
    
          
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        node = Trie()
        for word in words:
            node.insert(word)
        return node.getResult()
            
        
        