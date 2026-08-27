class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


    def insert(self, word: str) -> None:
        current = self
        for c in word:
            index = ord(c) - ord('a')
            if current.children[index] is None : 
                current.children[index] = PrefixTree()
            current = current.children[index]
        current.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        current = self
        for c in word:
            index = ord(c) - ord('a')
            if current.children[index] is None: 
                return False
            current = current.children[index]
        return current.isEndOfWord 


    def startsWith(self, prefix: str) -> bool:
        current = self
        for c in prefix:
            index = ord(c) - ord('a')
            if current.children[index] is None: 
                return False
            current = current.children[index]
        return True
        
        