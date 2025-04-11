class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - 97
            if node.children[idx] == None:
                newNode = TrieNode()
                node.children[idx] = newNode

            node = node.children[idx]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            idx = ord(ch) - 97
            if node.children[idx] == None:
                return False

            node = node.children[idx]
        return node.isEndOfWord
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            idx = ord(ch) - 97
            if node.children[idx] == None:
                return False

            node = node.children[idx]
        return True
