"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/1317360489/

TC: O(n)
SC: O(n)

Type: Stack, BST, DFS
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        ## Inorder traversal
        count = 0
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            count += 1
            if count == k:
                return current.val
            
            current = current.right

            
        
