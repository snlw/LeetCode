"""
https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/1285956299/

Time Complexity: O(height)
Space Complexity: O(height)

Type: BFS
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = []
        
        def bfs(root, row = 0):
            if root is None:
                return
            
            if len(order) < row + 1:
                order.append([])
            
            order[row].append(root.val)
            
            bfs(root.left, row + 1)
            bfs(root.right, row + 1)

        bfs(root)

        return order
