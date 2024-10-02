"""
https://leetcode.com/problems/rank-transform-of-an-array/submissions/1409452002/?envType=daily-question&envId=2024-10-02
"""
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        sortedValueWithIndex = sorted(enumerate(arr), key=lambda x: x[1])
        ans = [0] * n
        rank = 1

        for i in range(n):
            idx, curr = sortedValueWithIndex[i]
            if i == 0:
                ans[idx] = rank
                rank += 1
            else:
                previous = sortedValueWithIndex[i - 1][1]
                if curr == previous:
                    ans[idx] = rank - 1
                else:
                    ans[idx] = rank
                    rank += 1
        return ans

        
