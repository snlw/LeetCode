# https://leetcode.com/problems/invert-binary-tree/submissions/1276369931/

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.swap(root)

        return root
    
    def swap(self, node: TreeNode):
        if node == None:
            return 
        else:

            # Swap L and R of children nodes
            self.swap(node.left)
            self.swap(node.right)

            # Swap L and R of current Node
            left = node.left
            right = node.right
            node.left = right
            node.right = left

