"""
https://leetcode.com/problems/binary-tree-postorder-traversal/?envType=daily-question&envId=2024-08-25

TC: O(n)
SC: O(n)

Type: DFS
"""
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)

        dfs(root)
        return ans
