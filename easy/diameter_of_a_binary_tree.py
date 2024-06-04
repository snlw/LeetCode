# https://leetcode.com/problems/diameter-of-binary-tree/submissions/1277550756/
# Time complexity: O(n)
# Space complexity: O(1)

# Type: Binary Tree, Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def getHeight(root: Optional[TreeNode]):
            nonlocal diameter 
            if root is None:
                return -1
            
            # Calculate number of nodes on the left of a node
            left = getHeight(root.left) + 1
            # Calculate number of nodes on the right of a node
            right = getHeight(root.right) + 1

            # Check the maximum diameter
            diameter = max(diameter, left + right)

            return max(left, right)

        getHeight(root)

        return diameter

        
        
