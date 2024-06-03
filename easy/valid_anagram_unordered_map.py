# https://leetcode.com/problems/valid-anagram/submissions/1276127105/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Type: Unordered Map
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = dict()

        for i in range(len(s)):
            if s[i] not in frequency.keys():
                frequency[s[i]] = 1
            else:
                frequency[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in frequency.keys():
                return False
            else:
                frequency[t[i]] -= 1
                if (frequency[t[i]] < 0):
                    return False

        return True   
