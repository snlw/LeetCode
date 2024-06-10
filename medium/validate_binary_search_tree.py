# https://leetcode.com/problems/validate-binary-search-tree/submissions/1283875439/

# Time Complexity: O(n)
# Space Complexity: O(height)

# Type: DFS, Recursion
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lower=float("-inf"), upper=float("inf")):
            if not root:
                return True
            
            if not lower < root.val < upper:
                return False

            return dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper)

        return dfs(root)
        
