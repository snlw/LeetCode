"""
https://leetcode.com/problems/path-sum/submissions/1316199964/

TC: O(n)
SC: O(1)

Type: DFS, Recursion
"""
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ## Empty Tree
        if root is None:
            return False

        ## Single Node
        if root.left is None and root.right is None:
            return root.val == targetSum

        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)    
        return left or right

        
