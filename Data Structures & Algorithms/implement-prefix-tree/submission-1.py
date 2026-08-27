class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if current.children[index] is None : 
                current.children[index] = TrieNode()
            current = current.children[index]
        current.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if current.children[index] is None: 
                return False
            current = current.children[index]
        return current.isEndOfWord 


    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if current.children[index] is None: 
                return False
            current = current.children[index]
        return True
        
        