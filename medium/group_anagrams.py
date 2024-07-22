"""
https://leetcode.com/problems/group-anagrams/submissions/1329596315/

TC: O(n)
SC: O(n)

Type: Hash Map
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        anagrams = dict()

        for s in strs:
            charsInSortedOrder = "".join(sorted([*s]))
            if charsInSortedOrder in anagrams:
                idx = anagrams[charsInSortedOrder]
                ans[idx].append(s)
            else:
                currentKeys = len(anagrams.keys())
                if currentKeys == 0:
                    anagrams[charsInSortedOrder] = 0
                else:
                    anagrams[charsInSortedOrder] = currentKeys 
                ans.append([s])

        return ans
