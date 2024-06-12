"""
https://leetcode.com/problems/permutations/submissions/1286057230/

Time Complexity: O(n * n!)
Space Complexity: O(n)

Type: Backtracking, Recursion, Permutations
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []

        def backtrack(left, right):
            if left == right:
                answer.append(nums[:])
                return
            
            for i in range(left, right):
                nums[left], nums[i] = nums[i], nums[left]
                backtrack(left + 1, right)
                nums[left], nums[i] = nums[i], nums[left]
        
        backtrack(0, n)
        return answer


