"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1286806109/

Time Complexity: O(n)
Space Complexity: O(n)

Type: DFS, Recursion
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            if root is None or root == p or root == q:
                return root

            leftTree = dfs(root.left, p, q)
            rightTree = dfs(root.right, p, q)

            if leftTree is not None and rightTree is not None:
                return root

            if leftTree is None:
                return rightTree
            else:
                return leftTree

        return dfs(root, p, q)
        
        
