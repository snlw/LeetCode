"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree/submissions/1323098162/?envType=study-plan-v2&envId=leetcode-75

TC: O(n)
SC: O(1)

Type: DFS
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root, mx):
            if root is None:
                return
            
            if root.val >= mx:
                nonlocal ans
                ans += 1
            
            dfs(root.left, max(mx, root.val))
            dfs(root.right, max(mx, root.val))

        dfs(root, float('-inf'))
        return ans

            
        
