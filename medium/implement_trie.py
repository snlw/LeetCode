"""
https://leetcode.com/problems/implement-trie-prefix-tree/submissions/1285742943/

Time Complexity: O(n)
Space Complexity: O(n)

Type: Trie
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.end = True

    def search(self, word: str) -> bool:
        root = self.root
        for char in word:
            if char not in root.children:
                return False
            root = root.children[char]
        return root.end

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for char in prefix:
            if char not in root.children:
                return False
            root = root.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
