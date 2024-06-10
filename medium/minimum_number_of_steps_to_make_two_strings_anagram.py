# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/submissions/1283595496/?envType=daily-question&envId=2024-06-10

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Hash Map
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sF = self.getFrequency(s)
        tF = self.getFrequency(t)

        ans = 0

        for key, value in sF.items():
            if key in tF.keys():
                if value > tF[key]:
                    ans += value - tF[key] 
            else:
                ans += value
        
        return ans

    
    def getFrequency(self, a: str):
        f = dict()

        for char in a:
            if char in f.keys():
                f[char] += 1
            else:
                f[char] = 1

        return f
        
