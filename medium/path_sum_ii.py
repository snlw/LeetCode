"""
https://leetcode.com/problems/path-sum-ii/submissions/1323126226/

TC: O(n)
SC: O(n)

Type: DFS
"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(root, carry):
            if root is None:
                return 

            if root.left is None and root.right is None:
                if sum(carry) + root.val == targetSum:
                    ans.append(carry + [root.val])
                return
            
            dfs(root.left, carry + [root.val])
            dfs(root.right, carry + [root.val])

        dfs(root, [])
        return ans
        
