# https://leetcode.com/problems/determine-if-two-strings-are-close/submissions/1283817542

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Hash Map
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if word1 == word2:
            return True
        # Operation 1: Swap any two existing characters.
        #   --> We can reorder the characters without a limit
        # Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
        #   --> We can freely assign frequencies
        w1F = self.getFrequency(word1)
        w2F = self.getFrequency(word2)

        if w1F == w2F:
            return True

        if w1F.keys() == w2F.keys() and sorted(w1F.values()) == sorted(w2F.values()):
            return True

        return False

    def getFrequency(self, word: str):
        f = dict()
        for char in word:
            if char in f.keys():
                f[char] += 1
            else:
                f[char] = 1
        return f
        
