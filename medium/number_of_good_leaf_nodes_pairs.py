"""
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/submissions/1324929912/?envType=daily-question&envId=2024-07-18

TC: O(n)
SC: O(l) where l is the number of leaves

Type: DFS, Binary Tree
"""
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # List(path: str)
        leaves = []
        def dfs(root, path):
            if root is None:
                return 

            if root.left is None and root.right is None:
                leaves.append(path)
                return
            
            dfs(root.left, path + "L")
            dfs(root.right, path + "R")
            return

        dfs(root, "")
        ans = 0

        for i in range(len(leaves) - 1):
            for j in range(i + 1, len(leaves)):
                first = leaves[i]
                second = leaves[j]
                for k in range(min(len(first), len(second))):
                    if first[k] != second[k]:
                        first = first[k:]
                        second = second[k:]
                        break
                if len(first + second) <= distance:
                    ans += 1
        return ans
