"""
https://leetcode.com/problems/reverse-words-in-a-string/submissions/1295664516

Time Complexity: O(n/2)
Space Complexity: O(w), where w is the number of words

Type: String
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()

        for i in range(len(words) // 2):
            words[i], words[len(words) - i - 1] = words[len(words) - i - 1].strip(), words[i].strip()

        return " ".join(words)
        
