# https://leetcode.com/problems/find-common-characters/submissions/1279064174

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Recursion
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return [char for char in words[0]]

        common = self.getFrequency(words[0])
        for i in range(1, len(words)):
            common = self.getCommonFrequency(common, self.getFrequency(words[i]))

        ans = []

        for k, v in common.items():
            for i in range(v):
                ans.append(k)

        return ans


    def getFrequency(self, word:str):
        f = dict()

        for char in word:
            if char in f:
                f[char] += 1
            else:
                f[char] = 1

        return f

    def getCommonFrequency(self, w1, w2):
        common = dict()
        allKeys = list(set(list(w1.keys()) + list(w2.keys())))
        for k in allKeys:
            if k in w1.keys() and k in w2.keys():
                common[k] = min(w1[k], w2[k])
        return common
