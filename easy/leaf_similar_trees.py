"""
https://leetcode.com/problems/leaf-similar-trees/submissions/1323088989/?envType=study-plan-v2&envId=leetcode-75

TC: O(n1 + n2)
SC: O(n1 + n2)

Type: DFS
"""
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1, leaves2 = [], []
        def dfs(root, leaves):
            if root.left is None and root.right is None:
                leaves.append(root.val)
                return 
            if root.left:
                dfs(root.left, leaves)
            if root.right:
                dfs(root.right, leaves)

            return
        
        dfs(root1, leaves1)
        dfs(root2, leaves2)
        return leaves1 == leaves2
        
