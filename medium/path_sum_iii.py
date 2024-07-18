"""
https://leetcode.com/problems/path-sum-iii/submissions/1324971131/?envtype=study-plan-v2&envid=leetcode-75%5C

TC: O(n ^ 2)
SC: O(n)

Type: BFS + DFS
"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        queue = collections.deque()
        queue.append(root)
        ans = 0

        def dfs(root, total):
            if total is not None and total == targetSum:
                nonlocal ans
                ans += 1

            if root is None:
                return
            carry = total if total is not None else 0
            dfs(root.left, carry + root.val)
            dfs(root.right, carry + root.val)
            return

        while queue:
            node = queue.popleft()
            dfs(node, None)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return ans // 2


        

        
