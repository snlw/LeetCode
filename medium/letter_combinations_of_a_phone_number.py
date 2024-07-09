"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1315363796/

TC: O(n)
SC: O(1)

Type: Recursion, Backtracking
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)

        keys = dict({
            "2" : ['a', 'b', 'c'],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        })

        ans = []
        if len(digits) == 0:
            return ans

        def dfs(idx, s):
            if idx >= n:
                ans.append(s)
                return
            newCharacters = keys[digits[idx]]
            for c in newCharacters:
                dfs(idx + 1, s + c)

        dfs(0, "")
        return ans
        

        
