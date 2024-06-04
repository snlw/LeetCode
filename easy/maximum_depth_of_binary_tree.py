# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/1277479224/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Binary Tree, Recursion, DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth: int = 0) -> int:
        if root is None:
            return depth
        
        depth += 1

        left = self.maxDepth(root.left, depth)
        right = self.maxDepth(root.right, depth)

        return max(left, right)
        
