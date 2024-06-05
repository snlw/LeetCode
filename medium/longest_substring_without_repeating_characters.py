# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1278287023/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: String
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = ""

        longest = ""

        for char in s:
            if char in longest:
                if len(longest) > len(answer):
                    answer = longest

                idx = longest.find(char)
                longest = longest[idx+1:]

            longest += char

        return max(len(answer), len(longest))
                
        
