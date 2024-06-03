# https://leetcode.com/problems/balanced-binary-tree/submissions/1276395605/

# Time Complexity: O(n)
# Space Complexity: O(height of tree)

# Type: Binary Tree, Recursion, DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        self.checkNodeHeight(root)

        return self.isBalanced

    def checkNodeHeight(self, node: Optional[TreeNode]):
        if node is None:
            return 0 
        
        leftHeight = self.checkNodeHeight(node.left)
        rightHeight = self.checkNodeHeight(node.right)

        if abs(rightHeight - leftHeight) > 1:
            self.isBalanced = False

        return max(rightHeight, leftHeight) + 1
        
