"""
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/?envType=daily-question&envId=2024-08-06

TC: O(n)
SC: O(n)

Type: HashMap
"""
class Solution:
    def minimumPushes(self, word: str) -> int:
        f = {}
        for char in word:
            if char not in f:
                f[char] = 0
            f[char] += 1
        
        sortByFreq = sorted(f.items(), key=lambda x:x[1], reverse=True)
        ans = 0
        base = 1
        filledCounter = 0
        for key, count in sortByFreq:
            ans += base * count
            filledCounter += 1
            if filledCounter % 8 == 0:
                base += 1
        return ans
