"""
https://leetcode.com/problems/count-number-of-teams/submissions/1336803697/?envType=daily-question&envId=2024-07-29

TC: O(n ^ 2)
SC: O(1)

Type: DP 
* Optimized solution O(n log n) requires Binary Index Tree or Fenwick Tree
"""
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0

        ## Brute Force hits TLE for O(n^3) TC
        # for i in range(n - 2):
        #     for j in range(i + 1, n - 1):
        #         for k in range(j + 1, n):
        #             if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
        #                 ans += 1

        for mid in range(1, n - 1):
            leftLess, leftMore = 0, 0
            rightLess, rightMore = 0, 0
            for l in range(0, mid):
                if rating[l] < rating[mid]:
                    leftLess += 1
                elif rating[l] > rating[mid]:
                    leftMore += 1
            for r in range(mid + 1, n):
                if rating[r] < rating[mid]:
                    rightLess += 1
                elif rating[r] > rating[mid]:
                    rightMore += 1
            ans += leftLess*rightMore + rightLess*leftMore

        return ans

        
