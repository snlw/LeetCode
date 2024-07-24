"""
https://leetcode.com/problems/range-sum-of-bst/submissions/1331898717/

TC: O(n)
SC: O(height)

Type: DFS, BST
"""
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0

        def dfs(root):
            if root is None:
                return
            value = root.val
            if low <= value <= high:
                nonlocal ans
                ans += value
                dfs(root.left)
                dfs(root.right)
            elif value < low:
                dfs(root.right)    
            elif value > high:
                dfs(root.left)
            return

        dfs(root)

        return ans
        
