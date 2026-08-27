class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.EndOfWord = False

class Solution:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if current.children[index] is None:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.EndOfWord = True


    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for text in strs:
            self.insert(text)
        prefix = ""
        index = None
        current = self.root
        while True:
            count = 0
            for i, child in enumerate(current.children):
                if child is not None:
                    index = i
                    count += 1
            if current.EndOfWord == True or count > 1:
                break
            prefix += chr(ord('a') + index)
            current = current.children[index]
        return prefix
            




        

