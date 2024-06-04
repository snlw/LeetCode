# https://leetcode.com/problems/longest-palindrome/submissions/1277290258/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Hashmap
class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency = dict()

        for char in s:
            if char in frequency.keys():
                frequency[char] += 1
            else:
                frequency[char] = 1
        
        # Get number of pairs
        pairs = sum([f // 2 for f in frequency.values()])

        oddExists = int(any(f % 2 == 1 for f in frequency.values()))

        return oddExists + 2* pairs
        
