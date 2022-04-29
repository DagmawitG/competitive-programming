class Node:
    def __init__(self):
        self.children = [None]*26
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = Node()
    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            index = ord(char)-ord('a')
            if  current.children[index] is None:
                
                current.children[index] = Node()
            current = current.children[index]
        current.isWord = True    
    def search(self, word: str,isPrefix=False) -> bool:
        current = self.root
        for char in word:
            index = ord(char)-ord('a')
            if  current.children[index] is None:
                return False
            current = current.children[index]
          
            
    
        if current.isWord == True or isPrefix:
            return True
        else:
            return False
    
    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix,True)
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)