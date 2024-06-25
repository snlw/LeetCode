"""
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/submissions/1299645708

Time Complexity: O(height)
Space Complexity: O(height)

Type: Recursion
"""
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def dfs(root, fromRightTree = 0):
            if root is None:
                return 0 
            
            original = root.val
            
            right = dfs(root.right, fromRightTree)
            left = dfs(root.left, right + original + fromRightTree)
            
            root.val += right + fromRightTree

            return left + right + original

        dfs(root)

        return root

        
