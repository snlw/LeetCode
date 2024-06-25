"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/submissions/1299925794/?envType=study-plan-v2&envId=leetcode-75

Time Complexity: O(n)
Space Complexity: O(1)

Type: Sliding Window
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u']

        windowCount = len([c for c in s[:k] if c in vowels])
        ans = windowCount

        for i in range(k, n):
            if s[i] in vowels:
                if s[i - k] not in vowels:
                    windowCount += 1
            elif s[i - k] in vowels:
                windowCount -= 1
            ans = max(ans, windowCount)

        return ans

        
