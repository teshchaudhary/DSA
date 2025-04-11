from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.endCount = 0 

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.endCount += 1

    def getNode(self, prefix: str) -> TrieNode:
        node = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return None
            node = node.children[idx]
        return node

    def countWordsWithPrefix(self, node: TrieNode) -> int:
        if node is None:
            return 0
        count = node.endCount
        for child in node.children:
            if child:
                count += self.countWordsWithPrefix(child)
        return count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        prefix_node = trie.getNode(pref)
        return trie.countWordsWithPrefix(prefix_node)
