# https://leetcode.com/problems/ransom-note/submissions/1277235186/

# Time Complexity: O(n + m)
# Space Complexity: O(n)

# Type: Unordered Map
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequency = dict()

        for char in magazine:
            if char in frequency.keys():
                frequency[char] += 1
            else:
                frequency[char] = 1
        
        for char in ransomNote:
            if char in frequency.keys():
                frequency[char] -= 1
            else:
                return False

        return all( f >= 0 for f in frequency.values())
        
